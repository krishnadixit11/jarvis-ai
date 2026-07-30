import webbrowser
from core.logger import JarvisLogger


class BrowserAutomation:

    @staticmethod
    def open_youtube():
        JarvisLogger.info("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    @staticmethod
    def open_google():
        JarvisLogger.info("Opening Google...")
        webbrowser.open("https://www.google.com")

    @staticmethod
    def open_github():
        JarvisLogger.info("Opening GitHub...")
        webbrowser.open("https://github.com")