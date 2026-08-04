import os
import ctypes
from datetime import datetime

import pyautogui

try:
    from PIL import ImageGrab
except ImportError:
    ImageGrab = None

from core.logger import JarvisLogger


class SystemControl:

    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.03

    # =====================================
    # Internal Helper
    # =====================================

    @staticmethod
    def _press(key):

        try:

            pyautogui.press(key)

            JarvisLogger.success(
                f"Pressed : {key}"
            )

            return f"Pressed {key}."

        except Exception as e:

            JarvisLogger.error(
                f"Key Press Error : {e}"
            )

            return "Unable to press key."

    # =====================================
    # Volume
    # =====================================

    @staticmethod
    def volume_up():

        return SystemControl._press("volumeup")

    @staticmethod
    def volume_down():

        return SystemControl._press("volumedown")

    @staticmethod
    def mute_volume():

        return SystemControl._press("volumemute")

    # =====================================
    # Screenshot
    # =====================================

    @staticmethod
    def take_screenshot():

        if ImageGrab is None:

            return "Pillow is not installed."

        try:

            folder = os.path.join(
                os.getcwd(),
                "screenshots"
            )

            os.makedirs(
                folder,
                exist_ok=True
            )

            filename = datetime.now().strftime(
                "%Y%m%d_%H%M%S.png"
            )

            path = os.path.join(
                folder,
                filename
            )

            image = ImageGrab.grab()

            image.save(path)

            JarvisLogger.success(
                f"Screenshot Saved : {path}"
            )

            return "Screenshot captured successfully."

        except Exception as e:

            JarvisLogger.error(
                f"Screenshot Error : {e}"
            )

            return "Unable to capture screenshot."

    # =====================================
    # Lock PC
    # =====================================

    @staticmethod
    def lock_pc():

        try:

            ctypes.windll.user32.LockWorkStation()

            JarvisLogger.success(
                "PC Locked"
            )

            return "Locking your computer."

        except Exception as e:

            JarvisLogger.error(
                f"Lock Error : {e}"
            )

            return "Unable to lock computer."

    # =====================================
    # Type Text
    # =====================================

    @staticmethod
    def type_text(text):

        try:

            pyautogui.write(
                text,
                interval=0.02
            )

            JarvisLogger.success(
                f"Typed : {text}"
            )

            return f"Typed {text}."

        except Exception as e:

            JarvisLogger.error(
                f"Typing Error : {e}"
            )

            return "Unable to type."

    # =====================================
    # Hotkeys
    # =====================================

    @staticmethod
    def _hotkey(*keys):

        try:

            pyautogui.hotkey(*keys)

            JarvisLogger.success(
                f"Hotkey : {' + '.join(keys)}"
            )

            return "Done."

        except Exception as e:

            JarvisLogger.error(
                f"Hotkey Error : {e}"
            )

            return "Unable to perform shortcut."

    @staticmethod
    def copy():
        return SystemControl._hotkey("ctrl", "c")

    @staticmethod
    def paste():
        return SystemControl._hotkey("ctrl", "v")

    @staticmethod
    def cut():
        return SystemControl._hotkey("ctrl", "x")

    @staticmethod
    def undo():
        return SystemControl._hotkey("ctrl", "z")

    @staticmethod
    def redo():
        return SystemControl._hotkey("ctrl", "y")

    @staticmethod
    def select_all():
        return SystemControl._hotkey("ctrl", "a")

    @staticmethod
    def save_file():
        return SystemControl._hotkey("ctrl", "s")

    @staticmethod
    def new_file():
        return SystemControl._hotkey("ctrl", "n")

    @staticmethod
    def close_window():
        return SystemControl._hotkey("alt", "f4")

    @staticmethod
    def refresh():
        return SystemControl._press("f5")

    # =====================================
    # Individual Keys
    # =====================================

    @staticmethod
    def press_enter():
        return SystemControl._press("enter")

    @staticmethod
    def press_tab():
        return SystemControl._press("tab")

    @staticmethod
    def press_escape():
        return SystemControl._press("esc")

    @staticmethod
    def press_backspace():
        return SystemControl._press("backspace")

    @staticmethod
    def press_delete():
        return SystemControl._press("delete")

    @staticmethod
    def press_space():
        return SystemControl._press("space")

    @staticmethod
    def press_up():
        return SystemControl._press("up")

    @staticmethod
    def press_down():
        return SystemControl._press("down")

    @staticmethod
    def press_left():
        return SystemControl._press("left")

    @staticmethod
    def press_right():
        return SystemControl._press("right")