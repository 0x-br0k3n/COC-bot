import pyautogui
import time
import random
import win32api, win32con
import pytesseract
import re
from constants import ASSETS_DIR, CONFIDENCE, RANDOM_OFFSET

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 

def glide_to(x, y, duration=0.1):
    pyautogui.moveTo(x, y, duration=duration)

def swipe(start_x, start_y, end_x, end_y, duration=0.1):
    pyautogui.moveTo(start_x, start_y, duration=duration)
    pyautogui.dragTo(end_x, end_y, duration=duration)

def click(x, y):
    glide_to(x, y, duration=0.3)  # Glide to position before clicking
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def randomize_pos(x, y, offset=RANDOM_OFFSET):
    rx = x + random.randint(-offset, offset)
    ry = y + random.randint(-offset, offset)
    return rx, ry

def find_and_click(image_path, region=None, conf=CONFIDENCE):
    location = pyautogui.locateOnScreen(image_path, confidence=conf, region=region)
    if location is not None:
        center_x, center_y = pyautogui.center(location)
        rx, ry = randomize_pos(center_x, center_y)
        print(f"Found {image_path}, clicking at ({rx}, {ry})")
        click(rx, ry)
        return True
    return False

def capture_and_read_text(region):
    try:
        screenshot = pyautogui.screenshot(region=region)
        text = pytesseract.image_to_string(screenshot)
        return int(re.sub(r'[^0-9-]', '', text))
    except Exception as e:
        print(f"An error occurred during text recognition: {e}")
        return int("-1")
    