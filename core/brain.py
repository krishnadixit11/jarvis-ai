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
        
        if "screenshot" in command:
            return "TAKE_SCREENSHOT"

        if "lock computer" in command or "lock pc" in command:
            return "LOCK_PC"

        if "open camera" in command or "start camera" in command:
            return "OPEN_CAMERA"

        if "take photo" in command or "capture photo" in command:
            return "TAKE_PHOTO"
        
        if "increase volume" in command or "volume up" in command:
            return "VOLUME_UP"

        if "decrease volume" in command or "volume down" in command:
            return "VOLUME_DOWN"

        if "mute volume" in command or "mute" == command:
            return "MUTE_VOLUME"
        # ==========================
        # File Commands
        # ==========================

        if command in ["open desktop", "open my desktop"]:
            return "OPEN_DESKTOP"

        if command in ["open downloads", "open download", "downloads", "download"]:
            return "OPEN_DOWNLOADS"

        if command in ["open documents", "open document", "documents", "document"]:
            return "OPEN_DOCUMENTS"
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