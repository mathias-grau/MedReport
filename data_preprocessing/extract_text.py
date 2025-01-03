from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(f"Extracted text from {number_of_pages} pages.")
    return text


def extract_text_from_png(png_path):
    return "Simulated extracted text from png."


#### Test the functions
preprocessed_text = extract_text_from_pdf("../data/exemple.pdf")
print(preprocessed_text)