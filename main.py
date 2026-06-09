import threading
import time
import os
import sys
import keyboard
from PIL import Image
import pystray
from pystray import MenuItem as item
from src.skipper import check_and_skip

IS_RUNNING = False
PROGRAM_SHOULD_EXIT = False
tray_icon = None

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def skipper_loop():
    global IS_RUNNING, PROGRAM_SHOULD_EXIT
    print("[СИСТЕМА] Фоновый поток скиппера запущен.")
    
    while not PROGRAM_SHOULD_EXIT:
        if IS_RUNNING:
            try:
                check_and_skip()
            except Exception as e:
                print(f"[ОШИБКА СКИППЕРА] {e}")
        time.sleep(0.05)

def toggle_skipper(icon=None, item=None):
    global IS_RUNNING, tray_icon
    IS_RUNNING = not IS_RUNNING
    status = "АКТИВИРОВАН" if IS_RUNNING else "НА ПАУЗЕ"
    print(f"[СТАТУС] Скиппер переведен в режим: {status}")
    
    if tray_icon:
        tray_icon.title = f"Genshin Skipper ({status})"
        tray_icon.notify(f"Режим: {status}", "Genshin Skipper")

def exit_program(icon, item):
    global IS_RUNNING, PROGRAM_SHOULD_EXIT, tray_icon
    print("[СИСТЕМА] Закрытие программы...")
    IS_RUNNING = False
    PROGRAM_SHOULD_EXIT = True
    icon.stop()
    sys.exit(0)

def setup_tray():
    global tray_icon
    
    icon_path = resource_path(os.path.join("templates", "icon.png"))
    
    if os.path.exists(icon_path):
        image = Image.open(icon_path)
    else:
        print(f"[ВНИМАНИЕ] Иконка не найдена по пути: {icon_path}. Включаю синий квадрат.")
        image = Image.new('RGB', (64, 64), color='blue')
        
    menu = pystray.Menu(
        item('Вкл / Выкл (F8)', toggle_skipper),
        item('Выход', exit_program)
    )
    
    tray_icon = pystray.Icon("GenshinSkipper", image, "Genshin Skipper (НА ПАУЗЕ)", menu)
    tray_icon.run()

def main():
    global IS_RUNNING
    keyboard.add_hotkey('f8', toggle_skipper)
    
    logic_thread = threading.Thread(target=skipper_loop, daemon=True)
    logic_thread.start()
    
    print("[СИСТЕМА] Запуск иконки в трее...")
    setup_tray()

if __name__ == "__main__":
    main()