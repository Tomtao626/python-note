# coding: utf-8
# pdf编辑

import PyPDF4

# Parse the Text from PDF
def parse_text(pdf_file: str):
	reader = PyPDF4.PdfFileReader(pdf_file)
	for page in reader.pages:
		print(page.extractText())


# Remove Page from PDF
def remove_page(pdf_file: str, page_numbers: int):
	filer = PyPDF4.PdfReader('source.pdf', 'rb')
	out = PyPDF4.PdfWriter()
	for index in page_numbers:
		page = filer.pages[index]
		out.add_page(page)


with open('rm.pdf', 'wb') as f:
	out = PyPDF4.PdfWriter()
	out.write(f)


# Add Blank Page to PDF
def add_page(pdf_file: str, page_number: int):
	reader = PyPDF4.PdfFileReader(pdf_file)
	writer = PyPDF4.PdfWriter()
	writer.addPage()
	with open('add.pdf', 'wb') as f:
		writer.write(f)


# Rotate Pages
def rotate_page(pdf_file: str):
	reader = PyPDF4.PdfFileReader(pdf_file)
	writer = PyPDF4.PdfWriter()
	for page in reader.pages:
		page.rotateClockwise(90)
		writer.addPage(page)
	with open('rotate.pdf', 'wb') as f:
		writer.write(f)


# Merge PDFs
def merge_pdfs(pdf_file1, pdf_file2: str):
	pdf1 = PyPDF4.PdfFileReader(pdf_file1)
	pdf2 = PyPDF4.PdfFileReader(pdf_file2)
	writer = PyPDF4.PdfWriter()
	for page in pdf1.pages:
		writer.addPage(page)
	for page in pdf2.pages:
		writer.addPage(page)
	with open('merge.pdf', 'wb') as f:
		writer.write(f)
