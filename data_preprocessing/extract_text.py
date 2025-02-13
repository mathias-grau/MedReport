import os
from markitdown import MarkItDown
from PIL import Image
import pytesseract

def extract_text(file_path):
    """
    Use MarkItDown or a fallback. Or detect file type for PDF, PNG, etc.
    """
    # If pdf then use MarkItDown:
    if file_path.endswith('.pdf'):
        md = MarkItDown()
        result = md.convert(file_path)
        return result.text_content

    # If image then use pytesseract:
    elif file_path.endswith('.png') or file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        print(text)
        return text

    # If text file then read it:
    elif file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            return file.read()

    # If none of the above then return None:
    else:
        return None

