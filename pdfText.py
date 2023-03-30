import PyPDF2

with open("Pdf\Fees.pdf", "rb") as pdf_file:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    final_pdf_text = ""
    for i in range(number_of_pages):
        page = read_pdf.pages[i]
        page_content = page.extractText()
        final_pdf_text += page_content
print(final_pdf_text)





