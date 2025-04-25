from pdf2docx import Converter

pdf_path ="sample.pdf"
docx_path = "path"

cv = Converter(pdf_path)
cv.convert(docx_path)
cv.close()

print("PDF çevirildi")