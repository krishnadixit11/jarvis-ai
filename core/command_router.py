from datetime import datetime
from automation.file_manager import FileManager
from automation.browser import BrowserAutomation
from automation.windows import WindowsAutomation
from automation.system_control import SystemControl


class CommandRouter:

    def execute(self, action):

        # -----------------------------
        # Browser Commands
        # -----------------------------
        if isinstance(action, tuple):

            intent, value = action

            if intent == "OPEN_WEBSITE":
                return BrowserAutomation.open_website(value)

            if intent == "GOOGLE_SEARCH":
                return BrowserAutomation.google_search(value)

            if intent == "YOUTUBE_SEARCH":
                return BrowserAutomation.youtube_search(value)

        # -----------------------------
        # Windows Commands
        # -----------------------------
        if action == "OPEN_NOTEPAD":
            return WindowsAutomation.open_notepad()

        if action == "OPEN_CALCULATOR":
            return WindowsAutomation.open_calculator()

        if action == "OPEN_PAINT":
            return WindowsAutomation.open_paint()

        if action == "OPEN_CMD":
            return WindowsAutomation.open_cmd()

        if action == "OPEN_EXPLORER":
            return WindowsAutomation.open_explorer()

        # -----------------------------
        # File Commands
        # -----------------------------

        if action == "OPEN_DESKTOP":
          return FileManager.open_desktop()

        if action == "OPEN_DOWNLOADS":
          return FileManager.open_downloads()

        if action == "OPEN_DOCUMENTS": 
          return FileManager.open_documents()

        # -----------------------------
        # System Commands
        # -----------------------------
        if action == "TAKE_SCREENSHOT":
            return SystemControl.take_screenshot()

        if action == "LOCK_PC":
            return SystemControl.lock_pc()
        
        # -----------------------------
        # Utility Commands
        # -----------------------------
        if action == "GET_TIME":
            return datetime.now().strftime("Current time is %I:%M %p")

        if action == "GET_DATE":
            return datetime.now().strftime("Today is %d %B %Y")

        if action == "INTRO":
            return "I am Jarvis, your AI assistant."

        if action == "GREET":
            return "Hello Krishna."

        return None
        