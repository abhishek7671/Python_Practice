import pytesseract
from PIL import Image

# Specify the full path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_path =r"C:\Users\abhisheksu\Downloads\MicrosoftTeams-image (1).png"
img = Image.open(image_path)

text = pytesseract.image_to_string(img)

print(text)



