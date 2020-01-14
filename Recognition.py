"""
This file contains all the functions used to make the recognition with OCR

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

##### IMPORTS #####
import pytesseract
from PIL import Image

##### FUNCTIONS #####
def detect_number(img):
    """
    This function is used to make the recognition
    :param img: the processed image
    :return: the number recognized by OCR
    """
    image = Image.fromarray(img)
    text = pytesseract.image_to_string(image, config = '--dpi 300 --psm 11 -c tessedit_do_invert=0  -c tessedit_char_whitelist=0123456789')
    return text