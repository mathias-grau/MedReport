from PIL import Image
import pytesseract
image = Image.open('./data/exemple.png')
text = pytesseract.image_to_string( image )
print(text)