import PyPDF2

# 1. read a pdf files
f = open("Working_Business_Proposal.pdf", 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

print(pdf_reader.numPages)

page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
#print(page_one_text)
f.close()


# 2. read and write pdf files
f = open("Working_Business_Proposal.pdf", 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

print(pdf_reader.numPages)
first_page = pdf_reader.getPage(0)

pdf_writer = PyPDF2.PdfFileWriter()
print(type(first_page))
pdf_writer.addPage(first_page)

pdf_output = open("Some_BrandNew_Doc_2.pdf", "wb")
pdf_writer.write(pdf_output)

pdf_output.close()
f.close()

# 3. read entire pdf files
f = open("Working_Business_Proposal.pdf", 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

pdf_text = []
for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

print(pdf_text[0])
print(pdf_text[1])
