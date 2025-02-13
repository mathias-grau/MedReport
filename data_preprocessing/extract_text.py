import os
from PyPDF2 import PdfReader
from markitdown import MarkItDown

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)

    # This is a minimal example – you might want to read all pages, not just page[0]
    all_text = ""
    for i in range(number_of_pages):
        page = reader.pages[i]
        all_text += page.extract_text() + "\n"
    print(f"Extracted text from {number_of_pages} page(s).")
    return all_text

def extract_text_from_png(png_path):
    # Stub: you would implement OCR
    return "Simulated extracted text from png."

def extract_text(file_path):
    """
    Use MarkItDown or a fallback. Or detect file type for PDF, PNG, etc.
    """
    # If you are only using MarkItDown, do something:
    md = MarkItDown()
    result = md.convert(file_path)
    return result.text_content
