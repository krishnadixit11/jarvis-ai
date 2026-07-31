
import os
import pyautogui
import ctypes
from datetime import datetime

try:
    from PIL import ImageGrab
except ImportError:
    ImageGrab = None

from core.logger import JarvisLogger


class SystemControl:

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

    @staticmethod
    def take_screenshot():
        if ImageGrab is None:
            return "Pillow is not installed."

        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)

        filename = datetime.now().strftime("%Y%m%d_%H%M%S.png")
        path = os.path.join(folder, filename)

        image = ImageGrab.grab()
        image.save(path)

        JarvisLogger.info(f"Screenshot saved: {path}")

        return "Screenshot taken successfully."

    @staticmethod
    def lock_pc():
        JarvisLogger.info("Locking PC")
        ctypes.windll.user32.LockWorkStation()
        return "Locking your computer."