import fitz
import os

doc = fitz.open(r"C:\Users\ADMIN\Desktop\EasyOCR-master\easyocr\project.py\PUBLIC KEY INFRASTRUCTURE.pdf")
text = input("Enter the text to search: ")

for page in doc:
    text_instances = page.search_for(text)

    for inst in text_instances:
        highlight = page.add_highlight_annot(inst)
        highlight.update()

doc.save("highlighted.pdf", garbage=4, deflate=True, clean=True)
os.system("highlighted.pdf")

