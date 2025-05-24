import pytesseract
from PIL import Image
import cv2

def solve_captcha(image_path):
    img = Image.open(image_path)
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()