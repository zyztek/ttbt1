import cv2
import pytesseract
import numpy as np

class CaptchaSolver:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Ajustar para Windows
    
    def solve(self, image_path):
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
        text = pytesseract.image_to_string(opening, config='--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        return text.strip()