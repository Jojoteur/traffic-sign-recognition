import pytesseract
from PIL import Image
from sys import platform as _platform


if _platform == "linux" or _platform == "linux2":
    pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
elif _platform == "darwin":
    pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.0/bin/tesseract"
elif _platform == "win32":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
elif _platform == "win64":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def detect_number(img):
    image = Image.fromarray(img)
    result = pytesseract.image_to_string(image, config='--dpi 50') #Try different values
    return result