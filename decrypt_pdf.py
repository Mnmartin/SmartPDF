import PyPDF2

pdf_reader = PyPDF2.PdfReader(open('file_with_password.pdf', 'rb'))

if pdf_reader.is_encrypted:
    pdf_reader.decrypt('0000')

pdf_writer = PyPDF2.PdfWriter()

for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])

with open('file_without_password.pdf', 'wb') as pdf_file:
    pdf_writer.write(pdf_file)
