from pypdf import *

pdf_reader = PdfReader('./Gs_Resume.pdf')

print(f"total number of pages:{len(pdf_reader.pages)}")

full_text = ""

for page in pdf_reader.pages:
    full_text += page.extract_text() + "\n"
print(full_text)




