import pytesseract
from PIL import Image




def detect_number(img):
    image = Image.fromarray(img)
    text = pytesseract.image_to_string(image, config="--dpi 300") #Try different values
    return text