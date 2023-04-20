# -*- coding: utf-8 -*-
import pprint
import re
import time
import traceback
from urllib import parse as urlparse
import requests, chardet
import cchardet
import lxml
import lxml.html
from lxml.html import HtmlComment
from lxml import etree
from bs4 import BeautifulSoup

REGEXES = {
	'okMaybeItsACandidateRe': re.compile(
		'and|article|artical|body|column|main|shadow', re.I),
	'positiveRe': re.compile(
		('article|arti|body|content|textarea|entry|hentry|main|page|'
		 'artical|zoom|arti|context|message|editor|'
		 'pagination|post|txt|text|blog|story|post_body|post_content'), re.I),
	'negativeRe': re.compile(
		('copyright|combx|comment|com-|contact|foot|footer|footnote|decl|copy|'
		 'notice|'
		 'masthead|media|meta|outbrain|promo|related|scroll|link|pagebottom|bottom|'
		 'other|shoutbox|sidebar|sponsor|shopping|tags|tool|widget'), re.I),
}


class MainContent:
	def __init__(self, url='', gethtml=False, getxpath=False, getimgsrc=False, getimgbase64=False, headers=None,
	             cookies=None):

		if not url:
			raise 'pls input url'
		self.url = url
		self.titleCut = True
		self.gethtml = gethtml
		self.headers = headers
		self.cookies = cookies
		self.non_content_tag = set([
			'head',
			'meta',
			'script',
			'style',
			'object', 'embed',
			'iframe',
			'marquee',
			'select',
		])
		self.getXpath = getxpath
		self.getimgsrc = getimgsrc
		self.getimgbase64 = getimgbase64
		self.browcharset = {}

		self.title = ''
		self.p_space = re.compile(r'\s')
		self.p_html = re.compile(r'<html|</html>', re.IGNORECASE | re.DOTALL)
		self.p_content_stop = re.compile(r'正文.*结束|正文下|相关阅读|声明|分享让更多人看到|【\d】|本文来源：')
		self.p_clean_tree = re.compile(r'author|post-add|copyright')

	def get_title(self, doc):
		title = ''
		title_el = doc.xpath('//title')
		if title_el:
			title = title_el[0].text_content().strip()
			xpath = '//title'

		if len(title) < 7:
			tt = doc.xpath('//meta[@name="title"]')
			if tt:
				title = tt[0].get('content', '')
				xpath = '//meta[@name="title"]/@content'

		if len(title) < 7:
			tt = doc.xpath('//*[contains(@id, "title") or contains(@class, "title")]')
			xpath = '//*[contains(@id, "title") or contains(@class, "title")]'

			if not tt:
				tt = doc.xpath('//*[contains(@id, "font01") or contains(@class, "font01")]')
				xpath = '//*[contains(@id, "font01") or contains(@class, "font01")]'

			for t in tt:
				ti = t.text_content().strip()
				if ti in title and len(ti) * 2 > len(title):
					title = ti
					break
				if len(ti) > 20: continue
				if len(ti) > len(title) or len(ti) > 7:
					title = ti

		ddict = {}
		ddict['title'] = title
		ddict['title'] = ddict['title'].replace(u'\xa0', u' ')
		ddict['title_xpath'] = xpath

		return ddict

	def shorten_title(self, titledict):
		if self.titleCut:
			spliters = [' - ', '–', '—', '-', '|', '::']
			for s in spliters:
				if s not in titledict['title']:
					continue
				tts = titledict['title'].split(s)
				if len(tts) < 2:
					continue
				titledict['title'] = tts[0]
				break
			return titledict
		else:
			return titledict

	def calc_node_weight(self, node):

		weight = 1
		attr = '%s %s %s' % (
			node.get('class', ''),
			node.get('id', ''),
			node.get('style', '')
		)

		if attr.replace(' ', ''):
			mm = REGEXES['negativeRe'].findall(attr)
			weight -= 2 * len(mm)
			mm = REGEXES['positiveRe'].findall(attr)
			weight += 50 * len(mm)

		if node.tag in ['div', 'p', 'table']:
			weight += 2
		if node.text_content():
			weight += 2
			textlen = len(node.text_content())
			if textlen > 2999:
				weight += 20
			if textlen > 2499:
				weight += 15
			if textlen > 1999:
				weight += 10
			if textlen > 1999:
				weight += 5
			if textlen > 499:
				weight += 2


		s_chilrenxpathList = []
		if node.get('class', ''):
			chilrenxpath = '@class="%s"' % (node.get('class', ''))
			s_chilrenxpathList.append(chilrenxpath)
		if node.get('id', ''):
			chilrenxpath = '@id="%s"' % (node.get('id', ''))
			s_chilrenxpathList.append(chilrenxpath)
		if node.get('style', ''):
			chilrenxpath = '@style="%s"' % (node.get('style', ''))
			s_chilrenxpathList.append(chilrenxpath)

		xpath = ' and '.join(s_chilrenxpathList)
		if xpath:
			xpath1 = '//' + node.tag + '[' + xpath + ']'
		else:
			xpath1 = '//' + node.tag

		return weight, xpath1

	def get_main_block(self, url, html, short_title=True):
		''' return (title, etree_of_main_content_block)
		'''

		if isinstance(html, bytes):
			encoding = cchardet.detect(html)['encoding']
			if encoding is None:
				return None, None
			html = html.decode(encoding, 'ignore')
		try:
			doc = lxml.html.fromstring(html)
			doc.make_links_absolute(base_url=url)
		except:
			traceback.print_exc()
			return None, None
		self.title = self.get_title(doc)

		if short_title:
			self.title = self.shorten_title(self.title)
		body = doc.xpath('//body')

		if not body:
			return self.title, None
		candidates = []
		nodes = body[0].getchildren()
		while nodes:
			node = nodes.pop(0)
			children = node.getchildren()
			tlen = 0
			for child in children:
				if isinstance(child, HtmlComment):
					continue
				if child.tag in self.non_content_tag:
					continue
				if child.tag == 'a':
					continue
				if child.tag == 'textarea':
					# FIXME: this tag is only part of content?
					continue

				attr = '%s%s%s' % (child.get('class', ''),
				                   child.get('id', ''),
				                   child.get('style'))
				if 'display' in attr and 'none' in attr:
					continue
				nodes.append(child)
				if child.tag == 'p':
					weight = 3
				else:
					weight = 1

				text = '' if not child.text else child.text_content().strip()
				tail = '' if not child.tail else child.tail.strip()

				tlen += (len(text) + len(tail)) * weight
			if tlen < 10:
				continue
			weight, xpath = self.calc_node_weight(node)
			# print(weight,xpath)
			# print("text({}) + tail({}) * weigt({}) = {}".format(len(text),len(tail),weight,(len(text)+len(tail))*weight))
			candidates.append((node, tlen * weight, xpath))


		if not candidates:
			return self.title, None
		candidates.sort(key=lambda a: a[1], reverse=True)
		# print(candidates)
		good = candidates[0][0]

		if good.tag in ['p', 'pre', 'code', 'blockquote']:
			for i in range(5):
				good = good.getparent()
				if good.tag == 'div':
					break
		contentxpath = candidates[0][2]
		good = self.clean_etree(good, url)
		return self.title, good, contentxpath

	def clean_etree(self, tree, url=''):
		to_drop = []
		drop_left = False
		for num, node in enumerate(tree.iterdescendants()):
			if not node.text:
				continue
			if self.p_content_stop.search(node.text):
				drop_left = True
			if drop_left:
				to_drop.append(node)
				continue
			if isinstance(node, HtmlComment):
				to_drop.append(node)
				continue
			if node.tag in self.non_content_tag:
				to_drop.append(node)
				continue
			attr = '%s %s' % (
				node.get('class', ''),
				node.get('id', '')
			)
			if self.p_clean_tree.search(attr):
				to_drop.append(node)
				continue
			aa = node.xpath('.//a')
			if aa:
				text_node = len(self.p_space.sub('', node.text_content()))
				text_aa = 0
				for a in aa:
					alen = len(self.p_space.sub('', a.text_content()))
					if alen > 5:
						text_aa += alen
				if text_aa > text_node * 0.4:
					to_drop.append(node)
		for node in to_drop:
			try:
				node.drop_tree()
			except:
				pass
		return tree

	def img_to_base64(self, imgurl):
		import base64
		imgcode = requests.get(url=imgurl).content
		base64_data = base64.b64encode(imgcode)
		return str(base64_data, 'utf-8')


	def replaceHtml(self,html):
		p = re.compile(r"<table(.*?)>")
		html = p.sub('<table border="1">',html)
		p = re.compile(r"<tr(.*?)>")
		html = p.sub('<tr>',html)
		p = re.compile(r"<td(.*?)>")
		html = p.sub('<td>',html)
		p = re.compile(r"<th(.*?)>")
		html = p.sub('<th>',html)
		p = re.compile(r"<input(.*?)>")
		html = p.sub('',html)
		return html.replace(u'&#13;',u'').replace(u'\xa0',u'')

	def get_text(self, doc):
		lxml.etree.strip_elements(doc, 'script')
		lxml.etree.strip_elements(doc, 'style')
		for ch in doc.iterdescendants():
			if not isinstance(ch.tag, str):
				continue
			if ch.tag in ['img']:
				if self.getimgsrc and self.gethtml:
					ch.text = '\n' + '<img src="' + ch.get('src') + '">' + '\n'
					if self.getimgbase64:
						base64ImgCode = self.img_to_base64(ch.get('src'))
						ch.text = '\n' + '<img src="data:image/png;base64,' + base64ImgCode + '"/>' + '\n'
				if self.getimgsrc and not self.gethtml:
					ch.text = '\n' + '图片：' + ch.get('src') + '\n'
				if not self.getimgsrc:
					pass
			if ch.tag in ['div', 'h1', 'h2', 'h3', 'p', 'br', 'table', 'tr', 'dl', 'img']:
				if not ch.tail:
					ch.tail = '\n'
				else:
					ch.tail = '\n' + ch.tail.strip() + '\n'

			# if ch.tag in ['th', 'td','tr','table']:
			if ch.tag in ['table']:
				enHtml = etree.tostring(ch, encoding=self.browcharset['encoding'], pretty_print=True)
				cleanTable = self.replaceHtml(enHtml.decode(self.browcharset['encoding']))
				ch.text = cleanTable.replace('\n','')

		lines_a = doc.text_content().split('\n')
		lines = []
		for l in lines_a:
			strWord = l.replace('\t', '').strip()
			if strWord:
				if self.gethtml:
					lines.append('<p>' + strWord + '</p>')
				else:
					lines.append(strWord)
		if self.gethtml:
			return ''.join(lines)
		else:
			return '\n'.join(lines)

	def extract(self):
		'''return (title, content)
		'''

		ddict = {}
		try:
			brow = requests.get(self.url, headers=self.headers, cookies=self.cookies, timeout=(10, 10))
		except Exception as errormsg:
			print(errormsg)
			return None

		browEnCode = brow.text.encode(encoding=brow.encoding,errors='ignore')
		self.browcharset = chardet.detect(browEnCode)
		# print(self.browcharset)
		html = browEnCode.decode(self.browcharset['encoding'], 'ignore')

		titledict, node, content_xpath = self.get_main_block(self.url, html)
		if node is None:
			print('\tno main block got !!!!!', self.url)
			return titledict, '', ''

		ddict['title_artle'] = titledict['title']
		ddict['contentcharset'] = self.browcharset['encoding']

		ddict['page_url'] = self.url
		if self.getXpath:
			ddict['title_xpath'] = titledict['title_xpath']
			ddict['content_xpath'] = content_xpath
		content = self.get_text(node).replace(u'\xa0',u'')
		foot = '''
		<p>本文标题：<b>{title}</b></p>
		<p>本文标题xpath：<b>{title_xpath}</b></p>
		<p>本文链接：<b>{page_url}</b></p>
		<p>本文编码：<b>{contentcharset}</b></p>
		<p>本文内容xpath：<b>{content_xpath}</b></p>
		'''.format(title=ddict['title_artle'],title_xpath=ddict['title_xpath'],
		           page_url=ddict['page_url'],contentcharset=ddict['contentcharset'],
		           content_xpath=ddict['content_xpath'])
		soup = BeautifulSoup(content +"<HR>"+ foot,'lxml')
		ddict['content'] = soup.prettify()
		return ddict


if __name__ == '__main__':

	urlList = [
		"http://j.people.com.cn/n3/2021/0823/c94475-9887142.html",
		"https://news.sina.com.cn/o/2021-10-11/doc-iktzscyx8994384.shtml",
		"https://new.qq.com/rain/a/20211011A00OU300",
		"https://www.sohu.com/a/494438199_115376?spm=smpc.home.top-news3.6.16339410910292S1XphI&_f=index_news_11",
		"http://news.cn/techpro/20211009/f24f56a8bf534e9190122821d92a9a8a/c.html"
	]
	for url in urlList:
		MainC = MainContent(url=url)
		MainC.getimgsrc = False
		MainC.gethtml = True
		MainC.titleCut = False
		# a.getimgbase64 = True
		MainC.getXpath = True
		b = MainC.extract()
		pprint.pprint(b)
		print('*'*60)