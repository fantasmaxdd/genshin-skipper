import os
import sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

HOTKEY_TOGGLE = 'F8'
HOTKEY_EXIT = 'ctrl+alt+k'

CLICK_DELAY = 0.05
POST_CLICK_DELAY = 0.2

VISION_THRESHOLD = 0.82

TEMPLATE_DIALOG = os.path.join(TEMPLATES_DIR, 'dialog_icon.png')
TEMPLATE_OPTION = os.path.join(TEMPLATES_DIR, 'option_icon.png')