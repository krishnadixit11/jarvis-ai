from core.logger import JarvisLogger


class Brain:

    def process(self, command: str):

        command = command.lower().strip()

        JarvisLogger.info(
            f"Processing Command: {command}"
        )

        # ==========================
        # Memory Commands
        # ==========================

        if command.startswith("remember my "):
            return (
                "REMEMBER",
                command.replace("remember my ", "", 1).strip()
            )

        if command.startswith("what is my "):
            return (
                "RECALL",
                command.replace("what is my ", "", 1).strip()
            )

        if command.startswith("tell me my "):
            return (
                "RECALL",
                command.replace("tell me my ", "", 1).strip()
            )

        # ==========================
        # Typing
        # ==========================

        if command.startswith("type "):
            return (
                "TYPE_TEXT",
                command.replace("type ", "", 1).strip()
            )

        # ==========================
        # Keyboard Keys
        # ==========================

        keys = {
            "press enter": "PRESS_ENTER",
            "press tab": "PRESS_TAB",
            "press escape": "PRESS_ESCAPE",
            "press backspace": "PRESS_BACKSPACE",
            "press delete": "PRESS_DELETE",
            "press space": "PRESS_SPACE",
            "press up": "PRESS_UP",
            "press down": "PRESS_DOWN",
            "press left": "PRESS_LEFT",
            "press right": "PRESS_RIGHT",
        }

        if command in keys:
            return keys[command]

        # ==========================
        # Keyboard Shortcuts
        # ==========================

        shortcuts = {
            "copy": "COPY",
            "paste": "PASTE",
            "cut": "CUT",
            "undo": "UNDO",
            "redo": "REDO",
            "select all": "SELECT_ALL",
            "save": "SAVE_FILE",
            "save file": "SAVE_FILE",
            "new file": "NEW_FILE",
            "close window": "CLOSE_WINDOW",
            "refresh": "REFRESH",
        }

        if command in shortcuts:
            return shortcuts[command]

        # ==========================
        # File Search
        # ==========================

        if command.startswith("find "):
            return (
                "SEARCH_FILE",
                command.replace("find ", "", 1).strip()
            )

        if command.startswith("search file "):
            return (
                "SEARCH_FILE",
                command.replace("search file ", "", 1).strip()
            )

        if command.startswith("locate "):
            return (
                "SEARCH_FILE",
                command.replace("locate ", "", 1).strip()
            )

        # ==========================
        # File Manager
        # ==========================

        if command in [
            "open desktop",
            "open my desktop"
        ]:
            return "OPEN_DESKTOP"

        if command in [
            "open downloads",
            "downloads",
            "download"
        ]:
            return "OPEN_DOWNLOADS"

        if command in [
            "open documents",
            "documents",
            "document"
        ]:
            return "OPEN_DOCUMENTS"

        # ==========================
        # Alarm & Reminder
        # ==========================

        if command.startswith("set alarm for "):

            alarm_time = command.replace(
                "set alarm for ",
                "",
                1
            ).strip()

            return (
                "SET_ALARM",
                alarm_time
            )


        if command.startswith("remind me to "):

            text = command.replace(
                "remind me to ",
                "",
                1
            ).strip()


            if " at " in text:

                message, reminder_time = text.rsplit(
                    " at ",
                    1
                )

                return (
                    "SET_REMINDER",
                    (
                        message.strip(),
                        reminder_time.strip()
                    )
                )
        # ==========================
        # App Launcher
        # ==========================

        if command.startswith("open "):

            app = command.replace(
                "open ",
                "",
                1
            ).strip()

            known_apps = [

                # Browsers
                "chrome",
                "google chrome",
                "edge",
                "firefox",

                # Development
                "vscode",
                "visual studio code",
                "pycharm",
                "android studio",
                "git bash",

                # Windows
                "notepad",
                "calculator",
                "paint",
                "cmd",
                "command prompt",
                "explorer",
                "file explorer",
                "terminal",

                # Office
                "word",
                "excel",
                "powerpoint",

                # Communication
                "whatsapp",
                "telegram",
                "discord",

                # Media
                "spotify",
                "vlc",

                # Gaming
                "steam"
            ]

            if app in known_apps:
                return (
                    "OPEN_APP",
                    app
                )

        # ==========================
        # System Commands
        # ==========================

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

        if "mute volume" in command or command == "mute":
            return "MUTE_VOLUME"

        # ==========================
        # Browser
        # ==========================

        if command.startswith("search ") and " on google" in command:

            query = command.replace(
                "search ",
                "",
                1
            ).replace(
                " on google",
                ""
            ).strip()

            return (
                "GOOGLE_SEARCH",
                query
            )

        if command.startswith("search ") and " on youtube" in command:

            query = command.replace(
                "search ",
                "",
                1
            ).replace(
                " on youtube",
                ""
            ).strip()

            return (
                "YOUTUBE_SEARCH",
                query
            )

        if command.startswith("open "):

            website = command.replace(
                "open ",
                "",
                1
            ).strip()

            return (
                "OPEN_WEBSITE",
                website
            )

        # ==========================
        # Utility
        # ==========================

        if "time" in command:
            return "GET_TIME"

        if "date" in command:
            return "GET_DATE"

        if "battery" in command:
            return "GET_BATTERY"

        if "cpu" in command:
            return "GET_CPU"

        if "ram" in command or "memory usage" in command:
            return "GET_RAM"

        if "disk" in command or "storage" in command:
            return "GET_DISK"

        # ==========================
        # Greetings
        # ==========================

        if command in ["hello", "hi", "hey"]:
            return "GREET"

        if "who are you" in command:
            return "INTRO"

        # ==========================
        # Exit
        # ==========================

        if command in [
            "exit",
            "quit",
            "stop"
        ]:
            return "EXIT"

        # ==========================
        # AI Chat
        # ==========================

        return (
            "AI_CHAT",
            command
        )