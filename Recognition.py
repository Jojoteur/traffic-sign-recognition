"""
This file contains all the functions used to make the recognition with OCR

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

##### IMPORTS #####
import pytesseract
from PIL import Image
from sys import platform as _platform


##### FUNCTIONS #####
def detect_number(image):
    """
    This function is used to make the recognition
    :param image: the processed image
    :return: the number recognized by OCR
    """
    # Depending of the platform, the tesseract executable is not located at the same place
    if _platform == "linux" or _platform == "linux2":
        pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
    elif _platform == "darwin":
        pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.0/bin/tesseract"
    elif _platform == "win32":
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    elif _platform == "win64":
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    ready = Image.fromarray(image)
    config = r'--dpi 300 --psm 11 -c tessedit_char_whitelist=0123456789'
    config =""
    text = pytesseract.image_to_string(ready, config = config)
    " -psm 11 : Sparse text. Find as much text as possible in no particular order (See tesseract documentation) "
    " -c tessedit_char_whitelist=0123456789' : detect only digits "
    """
    !!!! It seems that whitelist doesn't work on Raspberry Pi !!!!
    """
    return text