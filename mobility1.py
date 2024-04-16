import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        img = img.resize((img.width * 2, img.height * 2))
        text = pytesseract.image_to_string(img, lang='eng')
        return text
    except FileNotFoundError:
        print("File not found. Please provide a valid image path.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

image_path = r"C:\Users\abhisheksu\Downloads\MicrosoftTeams-image (1).png"
extracted_text = extract_text_from_image(image_path)

if extracted_text:
    print("Text extracted from the image:")
    print(extracted_text)
else:
    print("No text could be extracted from the image.")
