import cv2
import numpy as np
import os
from PIL import ImageGrab
from config.settings import VISION_THRESHOLD

def take_screenshot():
    screenshot = ImageGrab.grab()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def find_template_on_screen(template_path, screenshot=None):
    if not os.path.exists(template_path):
        print(f"[ОШИБКА] Файл шаблона не найден: {template_path}")
        return None

    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        print(f"[ОШИБКА] Не удалось загрузить шаблон: {template_path}")
        return None
    
    w, h = template.shape[::-1]

    if screenshot is None:
        screenshot = take_screenshot()
    
    screen_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)

    if max_val >= VISION_THRESHOLD:
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        return (center_x, center_y)

    return None