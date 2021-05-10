#Install from pip: pip install pdf2docx
from pdf2docx import parse

#We define input and output route
pdf_file = '/path/to/sample.pdf'
docx_file = '/path/to/sample.docx'

#We convert the pdf to a docx file
parse(pdf_file, docx_file, start=0, end=1)
