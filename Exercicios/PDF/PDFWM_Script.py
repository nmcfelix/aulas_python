import PyPDF2
import sys
import os

output = PyPDF2.PdfFileWriter()

pdfWtrFile = open('.//Exercicios/PDF/wtr.pdf', 'rb')
watermark = PyPDF2.PdfFileReader(pdfWtrFile)
pdfSuperFile = open('.//Exercicios/PDF/super.pdf', 'rb')
pdfSuper = PyPDF2.PdfFileReader(pdfSuperFile)

for i in range(pdfSuper.getNumPages()):
    page = pdfSuper.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('.//Exercicios/PDF/WaterMArkedPdf.pdf', 'wb') as f:
    output.write(f)
