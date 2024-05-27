# pdf_processor.py

import PyPDF2

def process_pdf(file):
    text = ""
    with open(file.filename, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
