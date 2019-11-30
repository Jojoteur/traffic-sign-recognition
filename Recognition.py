import pytesseract
from PIL import Image

"""
## FOR MAC OS ##
pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.0/bin/tesseract"


## FOR WINDOWS ##
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

"""
## FOR RASPIAN ##
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"


def detect_number(img):
    image = Image.fromarray(img)
    result = pytesseract.image_to_string(image, config='--dpi 100')
    return result