import difflib

from core.logger import JarvisLogger


class Brain:

    def __init__(self):

        # ===========================
        # Known Applications
        # ===========================

        self.apps = [

            "chrome",
            "google chrome",
            "edge",
            "firefox",

            "vscode",
            "visual studio code",
            "pycharm",
            "android studio",

            "git bash",
            "terminal",
            "cmd",
            "command prompt",

            "calculator",
            "paint",
            "notepad",
            "explorer",
            "file explorer",

            "word",
            "excel",
            "powerpoint",

            "spotify",
            "vlc",

            "telegram",
            "discord",
            "whatsapp",

            "steam"

        ]

        # ===========================
        # Websites
        # ===========================

        self.websites = [

            "youtube",
            "google",
            "github",
            "chatgpt",
            "gmail",
            "linkedin",
            "facebook",
            "instagram",
            "reddit"

        ]

        # ===========================
        # App Launch Prefixes
        # ===========================

        self.launch_prefixes = [

            "open ",
            "launch ",
            "start ",
            "run "

        ]

        # ===========================
        # Wake Word Mistakes
        # ===========================

        self.wake_aliases = [

            "jarvis",
            "jarves",
            "jarviso",
            "jarviso",
            "jarvish",
            "jarvice",
            "jarviss"

        ]

    # ==================================================

    def best_match(self, word, options, cutoff=0.60):

        match = difflib.get_close_matches(
            word,
            options,
            n=1,
            cutoff=cutoff
        )

        return match[0] if match else None

    # ==================================================

    def normalize(self, command):

        command = command.lower().strip()

        command = " ".join(command.split())

        replacements = {

            "northpad": "notepad",
            "nodepad": "notepad",
            "note pad": "notepad",
            "node pad": "notepad",

            "vs code": "vscode",

            "command": "cmd",

            "google chrome": "chrome"

        }

        for wrong, right in replacements.items():

            command = command.replace(
                wrong,
                right
            )

        return command

    # ==================================================

    def process(self, command):

        command = self.normalize(command)

        JarvisLogger.info(
            f"Processing Command : {command}"
        )

        if not command:
            return None

        # =====================================
        # Remove accidental wake words
        # =====================================

        words = []

        for word in command.split():

            if word in self.wake_aliases:
                continue

            words.append(word)

        command = " ".join(words).strip()

        if not command:
            return None

        # =====================================
        # Memory
        # =====================================

        if command.startswith("remember my "):

            return (

                "REMEMBER",

                command.replace(
                    "remember my ",
                    "",
                    1
                ).strip()

            )

        if command.startswith("what is my "):

            return (

                "RECALL",

                command.replace(
                    "what is my ",
                    "",
                    1
                ).strip()

            )

        if command.startswith("tell me my "):

            return (

                "RECALL",

                command.replace(
                    "tell me my ",
                    "",
                    1
                ).strip()

            )

        # =====================================
        # Typing
        # =====================================

        if command.startswith("type "):

            return (

                "TYPE_TEXT",

                command.replace(
                    "type ",
                    "",
                    1
                ).strip()

            )

        # =====================================
        # Keyboard Keys
        # =====================================

        key_commands = {

            "press enter": "PRESS_ENTER",
            "press tab": "PRESS_TAB",
            "press escape": "PRESS_ESCAPE",
            "press backspace": "PRESS_BACKSPACE",
            "press delete": "PRESS_DELETE",
            "press space": "PRESS_SPACE",
            "press up": "PRESS_UP",
            "press down": "PRESS_DOWN",
            "press left": "PRESS_LEFT",
            "press right": "PRESS_RIGHT"

        }

        if command in key_commands:
            return key_commands[command]

        # =====================================
        # Keyboard Shortcuts
        # =====================================

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
            "refresh": "REFRESH"

        }

        if command in shortcuts:
            return shortcuts[command]

        # ======= Continue in Part 2 =======

                # =====================================
        # Alarm
        # =====================================

        if command.startswith("set alarm for"):
            return (
                "SET_ALARM",
                command.replace("set alarm for", "", 1).strip()
            )

        # =====================================
        # Reminder
        # =====================================

        if command.startswith("remind me to"):

            text = command.replace(
                "remind me to",
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

        # =====================================
        # App Launcher (Improved)
        # =====================================

        app_alias = {

            "northpad": "notepad",
            "note pad": "notepad",
            "nodepad": "notepad",
            "notepad": "notepad",

            "calc": "calculator",
            "calculator": "calculator",

            "paint": "paint",

            "chrome": "chrome",
            "google chrome": "chrome",

            "edge": "edge",

            "firefox": "firefox",

            "cmd": "command prompt",
            "terminal": "command prompt",
            "command prompt": "command prompt",

            "explorer": "file explorer",
            "file explorer": "file explorer",

            "spotify": "spotify",

            "telegram": "telegram",

            "discord": "discord",

            "whatsapp": "whatsapp",

            "vscode": "visual studio code",
            "vs code": "visual studio code",
            "visual studio code": "visual studio code",

            "pycharm": "pycharm",

            "android studio": "android studio",

            "steam": "steam",

            "word": "word",

            "excel": "excel",

            "powerpoint": "powerpoint",

            "vlc": "vlc"

        }

        app_prefixes = [

            "open ",
            "launch ",
            "start ",
            "run "

        ]

        for prefix in app_prefixes:

            if command.startswith(prefix):

                app = command.replace(
                    prefix,
                    "",
                    1
                ).strip()

                if app in app_alias:

                    return (
                        "OPEN_APP",
                        app_alias[app]
                    )

                from difflib import get_close_matches

                match = get_close_matches(
                    app,
                    list(app_alias.keys()),
                    n=1,
                    cutoff=0.60
                )

                if match:

                    return (
                        "OPEN_APP",
                        app_alias[match[0]]
                    )

        # =====================================
        # Browser Search
        # =====================================

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

        # =====================================
        # Website
        # =====================================

        website_alias = {

            "youtube": "youtube",
            "google": "google",
            "github": "github",
            "linkedin": "linkedin",
            "gmail": "gmail",
            "instagram": "instagram",
            "facebook": "facebook",
            "reddit": "reddit",
            "chatgpt": "chatgpt"

        }

        if command.startswith("open "):

            website = command.replace(
                "open ",
                "",
                1
            ).strip()

            if website in website_alias:

                return (
                    "OPEN_WEBSITE",
                    website_alias[website]
                )

        # =====================================
        # Camera
        # =====================================

        if command in [

            "open camera",
            "start camera"

        ]:

            return "OPEN_CAMERA"

        if command in [

            "take photo",
            "capture photo"

        ]:

            return "TAKE_PHOTO"

        # =====================================
        # Screenshot
        # =====================================

        if any(

            word in command

            for word in [

                "screenshot",
                "screen shot",
                "capture screen"

            ]

        ):

            return "TAKE_SCREENSHOT"

        # =====================================
        # Lock PC
        # =====================================

        if any(

            word in command

            for word in [

                "lock pc",
                "lock computer",
                "lock system"

            ]

        ):

            return "LOCK_PC"

        # =====================================
        # Volume
        # =====================================

        if any(

            word in command

            for word in [

                "volume up",
                "increase volume",
                "raise volume",
                "louder"

            ]

        ):

            return "VOLUME_UP"

        if any(

            word in command

            for word in [

                "volume down",
                "decrease volume",
                "lower volume"

            ]

        ):

            return "VOLUME_DOWN"

        if "mute" in command:

            return "MUTE_VOLUME"

        # =====================================
        # Utility
        # =====================================

        if "time" in command:
            return "GET_TIME"

        if "date" in command:
            return "GET_DATE"

        if "battery" in command:
            return "GET_BATTERY"

        if "cpu" in command:
            return "GET_CPU"

        if "ram" in command:
            return "GET_RAM"

        if "disk" in command:
            return "GET_DISK"

        # =====================================
        # Greetings
        # =====================================

        if command in [

            "hello",
            "hi",
            "hey"

        ]:

            return "GREET"

        if any(

            x in command

            for x in [

                "who are you",
                "introduce yourself"

            ]

        ):

            return "INTRO"

        # =====================================
        # Exit
        # =====================================

        if command in [

            "exit",
            "quit",
            "bye",
            "goodbye",
            "shutdown",
            "stop"

        ]:

            return "EXIT"

        # =====================================
        # AI
        # =====================================

        return (
            "AI_CHAT",
            command
        )