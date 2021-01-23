import PyPDF2
import re

f = open("Exercise_Files/Find_the_Phone_Number.pdf", "rb")

pdf_doc = PyPDF2.PdfFileReader(f)

#print(pdf_doc.numPages)

pattern3 = "\d{3,}(-|.| )\d{3,}(-|.| )\d{3,}"

for num in range(pdf_doc.numPages):
    page = pdf_doc.getPage(num)
    page_text = page.extractText()

    #print(page_text)
    for match in re.finditer(pattern3, page_text):
        print(match)
        print(match.group())

