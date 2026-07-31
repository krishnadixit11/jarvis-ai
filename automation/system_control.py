import os
import ctypes
import pyautogui
from datetime import datetime

try:
    from PIL import ImageGrab
except ImportError:
    ImageGrab = None

from core.logger import JarvisLogger


class SystemControl:


    # =====================================
    # Volume Control
    # =====================================

    @staticmethod
    def volume_up():

        pyautogui.press("volumeup")
        return "Volume increased."


    @staticmethod
    def volume_down():

        pyautogui.press("volumedown")
        return "Volume decreased."


    @staticmethod
    def mute_volume():

        pyautogui.press("volumemute")
        return "Volume muted."



    # =====================================
    # Screenshot
    # =====================================

    @staticmethod
    def take_screenshot():

        if ImageGrab is None:
            return "Pillow is not installed."


        folder = "screenshots"

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


        JarvisLogger.info(
            f"Screenshot saved: {path}"
        )


        return "Screenshot taken successfully."



    # =====================================
    # Lock PC
    # =====================================

    @staticmethod
    def lock_pc():

        JarvisLogger.info(
            "Locking PC"
        )

        ctypes.windll.user32.LockWorkStation()

        return "Locking your computer."



    # =====================================
    # Type Text
    # =====================================

    @staticmethod
    def type_text(text):

        JarvisLogger.info(
            f"Typing: {text}"
        )


        pyautogui.write(
            text,
            interval=0.03
        )


        return f"Typed: {text}"



    # =====================================
    # Keyboard Keys
    # =====================================

    @staticmethod
    def press_key(key):

        JarvisLogger.info(
            f"Pressing key: {key}"
        )


        pyautogui.press(key)


        return f"Pressed {key}."



    # =====================================
    # Keyboard Shortcuts
    # =====================================

    @staticmethod
    def copy():

        pyautogui.hotkey(
            "ctrl",
            "c"
        )

        return "Copied."


    @staticmethod
    def paste():

        pyautogui.hotkey(
            "ctrl",
            "v"
        )

        return "Pasted."


    @staticmethod
    def cut():

        pyautogui.hotkey(
            "ctrl",
            "x"
        )

        return "Cut."



    @staticmethod
    def undo():

        pyautogui.hotkey(
            "ctrl",
            "z"
        )

        return "Undo."



    @staticmethod
    def redo():

        pyautogui.hotkey(
            "ctrl",
            "y"
        )

        return "Redo."



    @staticmethod
    def select_all():

        pyautogui.hotkey(
            "ctrl",
            "a"
        )

        return "Selected all."



    @staticmethod
    def save_file():

        pyautogui.hotkey(
            "ctrl",
            "s"
        )

        return "File saved."



    @staticmethod
    def new_file():

        pyautogui.hotkey(
            "ctrl",
            "n"
        )

        return "New file created."



    @staticmethod
    def close_window():

        pyautogui.hotkey(
            "alt",
            "f4"
        )

        return "Window closed."



    @staticmethod
    def refresh():

        pyautogui.press(
            "f5"
        )

        return "Refreshed."