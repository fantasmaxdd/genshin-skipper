import time
import pydirectinput
from config.settings import POST_CLICK_DELAY

pydirectinput.PAUSE = 0.0

def press_space():
    pydirectinput.press('space')
    time.sleep(POST_CLICK_DELAY)

def click_at(x, y):
    original_x, original_y = pydirectinput.position()
    
    pydirectinput.click(x, y)
    
    pydirectinput.moveTo(original_x, original_y)
    time.sleep(POST_CLICK_DELAY)