# coding:utf-8
# 解析HTML

import gazpacho

# Extract HTML From Url
url = "https://www.tvmao.com/program"
html = gazpacho.get(url)
print(html)

# Extract HTML with Headers
headers = {'User-Agent': 'Mozilla/5.0'}
html = gazpacho.get(url, headers=headers)
print(html)

# Parse HTML
parse = gazpacho.Soup(html)

# Find single tags
tag1 = parse.find('h1')
tag2 = parse.find('span')

# Find multiple tags
tags1 = parse.find_all('p')
tags2 = parse.find_all('a')

# Find tags by class
tag = parse.find('.class')

# Find tags by Attribute
tag = parse.find("div", attrs={"class": "test"})
print(tag)

# Extract text from tags
text = parse.find('h1').text
text = parse.find_all('p')[0].text
print(text)
