from automation.browser import BrowserAutomation
from core.logger import JarvisLogger
from datetime import datetime


class CommandRouter:

    def execute(self, action):

        if action == "OPEN_YOUTUBE":
            BrowserAutomation.open_youtube()
            return "Opening YouTube."

        elif action == "OPEN_google":
            BrowserAutomation.open_google()
            return "Opening Google."

        elif action == "GET_TIME":
            current = datetime.now().strftime("%I:%M %p")
            JarvisLogger.info(current)
            return f"The time is {current}"

        elif action == "GET_DATE":
            current = datetime.now().strftime("%d %B %Y")
            return f"Today is {current}"

        elif action == "INTRO":
            return "I am Jarvis, your AI assistant."

        elif action == "GREET":
            return "Hello Krishna."

        elif action == "EXIT":
            return "Goodbye!"

        elif action == "AI_CHAT":
            return "Sorry, I don't know how to do that yet."

        return None