"""
This file contains all the functions used to make the recognition with OCR

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

##### IMPORTS #####
import pytesseract
from PIL import Image

##### FUNCTIONS #####
def detect_number(image):
    """
    This function is used to make the recognition
    :param image: the processed image
    :return: the number recognized by OCR
    """
    ready = Image.fromarray(image)
    text = pytesseract.image_to_string(ready, config = '--dpi 300 --psm 11  -c tessedit_char_whitelist=0123456789')
    " -psm 11 : Sparse text. Find as much text as possible in no particular order (See tesseract documentation) "
    " -c tessedit_char_whitelist=0123456789' : detect only digits "
    return text