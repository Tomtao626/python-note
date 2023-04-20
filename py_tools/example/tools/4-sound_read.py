# coding:utf-8
# 创建有声读物（pdf转音频）

from PyPDF2 import PdfFileReader as reader
from gtts import gTTS


def create_audio(pdf_file_conf: str):
	read_pdf = reader(pdf_file_conf, 'rb')
	for i in range(read_pdf.numPages):
		text = read_pdf.getPage(i).extract_text()
		tts = gTTS(text, lang="en")
		tts.save(f"page{str(i)}.mp3")


if __name__ == '__main__':
	create_audio("book.pdf")
