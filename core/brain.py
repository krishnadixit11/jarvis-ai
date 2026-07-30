from core.logger import JarvisLogger


class Brain:

    def process(self, command: str):

        command = command.lower().strip()

        JarvisLogger.info(f"Processing Command: {command}")

        # ==========================
        # Windows Commands
        # ==========================

        if "notepad" in command:
            return "OPEN_NOTEPAD"

        if "calculator" in command or "calc" in command:
            return "OPEN_CALCULATOR"

        if "paint" in command:
            return "OPEN_PAINT"

        if "command prompt" in command or "cmd" in command:
            return "OPEN_CMD"

        if "file explorer" in command or "explorer" in command:
            return "OPEN_EXPLORER"

        # ==========================
        # Browser Commands
        # ==========================

        if command.startswith("open "):
            website = command.replace("open ", "").strip()
            return ("OPEN_WEBSITE", website)

        if command.startswith("search ") and " on google" in command:
            query = command.replace("search ", "").replace(" on google", "").strip()
            return ("GOOGLE_SEARCH", query)

        if command.startswith("search ") and " on youtube" in command:
            query = command.replace("search ", "").replace(" on youtube", "").strip()
            return ("YOUTUBE_SEARCH", query)

        # ==========================
        # Utility Commands
        # ==========================

        if "time" in command:
            return "GET_TIME"

        if "date" in command:
            return "GET_DATE"

        # ==========================
        # Greetings
        # ==========================

        if "hello" in command or "hi" in command:
            return "GREET"

        if "who are you" in command:
            return "INTRO"

        # ==========================
        # Exit
        # ==========================

        if command in ["exit", "quit", "stop"]:
            return "EXIT"

        # ==========================
        # Default
        # ==========================

        return "AI_CHAT"