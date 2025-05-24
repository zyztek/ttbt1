import pytesseract
from PIL import Image
def solve_captcha(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text