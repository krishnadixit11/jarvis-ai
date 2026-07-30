import subprocess

from core.logger import JarvisLogger


class WindowsAutomation:

    @staticmethod
    def open_notepad():
        JarvisLogger.info("Opening Notepad")
        subprocess.Popen("notepad.exe")
        return "Opening Notepad."

    @staticmethod
    def open_calculator():
        JarvisLogger.info("Opening Calculator")
        subprocess.Popen("calc.exe")
        return "Opening Calculator."

    @staticmethod
    def open_paint():
        JarvisLogger.info("Opening Paint")
        subprocess.Popen("mspaint.exe")
        return "Opening Paint."

    @staticmethod
    def open_cmd():
        JarvisLogger.info("Opening Command Prompt")
        subprocess.Popen("cmd.exe")
        return "Opening Command Prompt."

    @staticmethod
    def open_explorer():
        JarvisLogger.info("Opening File Explorer")
        subprocess.Popen("explorer.exe")
        return "Opening File Explorer."