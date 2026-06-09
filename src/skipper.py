import pydirectinput
import time
import random
import pygetwindow as gw  # Библиотека для проверки активного окна
from config.settings import TEMPLATE_DIALOG, TEMPLATE_OPTION
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

    option_pos = find_template_on_screen(TEMPLATE_OPTION, screenshot)
    if option_pos:
        x, y = option_pos
        print(f"[СКИППЕР] Вижу облачко ответа в игре (X={x}, Y={y})")
        
        old_x, old_y = pydirectinput.position()
        
        target_x = x + 120 + random.randint(-15, 15)
        target_y = y + random.randint(-4, 4)

        pydirectinput.moveTo(target_x, target_y, duration=0.08)

        time.sleep(0.15) 

        pydirectinput.mouseDown(button='left')
        time.sleep(0.05)
        pydirectinput.mouseUp(button='left')
        print(f"[СКИППЕР] Надежный клик в точке ({target_x}, {target_y})")
 
        time.sleep(0.1)
        pydirectinput.moveTo(old_x, old_y, duration=0.04)

        time.sleep(0.5) 
        return True

    dialog_pos = find_template_on_screen(TEMPLATE_DIALOG, screenshot)
    if dialog_pos:
        human_press('space')
        print("[СКИППЕР] Прокрутка диалога (Space)...")
        time.sleep(0.12) 
        return True

    return False