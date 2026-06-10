import pydirectinput
import time
import random
import pygetwindow as gw
from config.settings import TEMPLATE_DIALOG, TEMPLATE_OPTION, VISION_THRESHOLD
from src.vision import take_screenshot, find_template_on_screen

pydirectinput.PAUSE = 0.0

def human_press(key, duration=0.05):
    pydirectinput.keyDown(key)
    time.sleep(duration)
    pydirectinput.keyUp(key)

def check_and_skip():
    try:
        active_window = gw.getActiveWindow()
        if active_window and "Genshin" not in active_window.title:
            return False
    except Exception:
        pass

    screenshot = take_screenshot()

    option_pos = find_template_on_screen(TEMPLATE_OPTION, screenshot, threshold=0.65)
    if option_pos:
        x, y = option_pos
        print(f"[СКИППЕР] Обнаружен выбор ответа в точке (X={x}, Y={y})")
        
        old_x, old_y = pydirectinput.position()
        
        target_x = x + 120 + random.randint(-15, 15)
        target_y = y + random.randint(-4, 4)
        
        pydirectinput.moveTo(target_x, target_y, duration=0.06)
        time.sleep(0.12) 
        
        pydirectinput.mouseDown(button='left')
        time.sleep(0.05)
        pydirectinput.mouseUp(button='left')
        print(f"[СКИППЕР] Успешный клик по варианту ответа.")
        
        time.sleep(0.08)
        pydirectinput.moveTo(old_x, old_y, duration=0.0)
        time.sleep(0.4) 
        return True

    dialog_pos = find_template_on_screen(TEMPLATE_DIALOG, screenshot, threshold=0.54)
    if dialog_pos:
        human_press('space')
        print("[СКИППЕР] Прокрутка диалога (Нажат Space)")
        time.sleep(0.15) 
        return True

    return False