from datetime import datetime

from core.ai_chat import AIChat
from core.memory import Memory
from core.logger import JarvisLogger

from automation.app_launcher import AppLauncher
from automation.browser import BrowserAutomation
from automation.camera import CameraAutomation
from automation.file_manager import FileManager
from automation.file_search import FileSearch
from automation.system_control import SystemControl
from automation.system_info import SystemInfo
from automation.windows import WindowsAutomation
from automation.alarm import AlarmManager


class CommandRouter:

    def __init__(self):

        self.memory = Memory()

        self.ai = AIChat()

    # ======================================================

    def execute(self, action):

        if action is None:
            return "Sorry Krishna, I didn't understand."

        try:

            # ==========================================
            # Commands with Parameters
            # ==========================================

            if isinstance(action, tuple):

                intent, value = action

                JarvisLogger.info(
                    f"Executing Intent : {intent}"
                )

                # ==================================
                # Memory
                # ==================================

                if intent == "REMEMBER":

                    parts = value.split(" is ", 1)

                    if len(parts) != 2:
                        return (
                            "Please tell me like "
                            "'remember my city is Delhi'."
                        )

                    key = parts[0].strip()

                    data = parts[1].strip()

                    return self.memory.remember(
                        key,
                        data
                    )

                if intent == "RECALL":

                    result = self.memory.recall(value)

                    if result:
                        return f"Your {value} is {result}."

                    return (
                        f"I don't remember your {value}."
                    )

                # ==================================
                # Browser
                # ==================================

                if intent == "OPEN_WEBSITE":

                    return BrowserAutomation.open_website(
                        value
                    )

                if intent == "GOOGLE_SEARCH":

                    return BrowserAutomation.google_search(
                        value
                    )

                if intent == "YOUTUBE_SEARCH":

                    return BrowserAutomation.youtube_search(
                        value
                    )

                # ==================================
                # Typing
                # ==================================

                if intent == "TYPE_TEXT":

                    return SystemControl.type_text(
                        value
                    )

                # ==================================
                # Applications
                # ==================================

                if intent == "OPEN_APP":

                    return AppLauncher.open_app(
                        value
                    )

                # ==================================
                # File Search
                # ==================================

                if intent == "SEARCH_FILE":

                    return FileSearch.search_file(
                        value
                    )

                # ==================================
                # Alarm
                # ==================================

                if intent == "SET_ALARM":

                    return AlarmManager.set_alarm(
                        value
                    )

                # ==================================
                # Reminder
                # ==================================

                if intent == "SET_REMINDER":

                    message, reminder_time = value

                    return AlarmManager.set_reminder(
                        reminder_time,
                        message
                    )

                # ==================================
                # AI
                # ==================================

                if intent == "AI_CHAT":

                    return self.ai.ask(value)

                            # ==========================================
            # Keyboard Keys
            # ==========================================

            key_actions = {

                "PRESS_ENTER": SystemControl.press_enter,
                "PRESS_TAB": SystemControl.press_tab,
                "PRESS_ESCAPE": SystemControl.press_escape,
                "PRESS_BACKSPACE": SystemControl.press_backspace,
                "PRESS_DELETE": SystemControl.press_delete,
                "PRESS_SPACE": SystemControl.press_space,
                "PRESS_UP": SystemControl.press_up,
                "PRESS_DOWN": SystemControl.press_down,
                "PRESS_LEFT": SystemControl.press_left,
                "PRESS_RIGHT": SystemControl.press_right,

            }

            if action in key_actions:

                JarvisLogger.info(
                    f"Executing : {action}"
                )

                return key_actions[action]()

            # ==========================================
            # Keyboard Shortcuts
            # ==========================================

            shortcut_actions = {

                "COPY": SystemControl.copy,
                "PASTE": SystemControl.paste,
                "CUT": SystemControl.cut,
                "UNDO": SystemControl.undo,
                "REDO": SystemControl.redo,
                "SELECT_ALL": SystemControl.select_all,
                "SAVE_FILE": SystemControl.save_file,
                "NEW_FILE": SystemControl.new_file,
                "CLOSE_WINDOW": SystemControl.close_window,
                "REFRESH": SystemControl.refresh,

            }

            if action in shortcut_actions:

                JarvisLogger.info(
                    f"Executing : {action}"
                )

                return shortcut_actions[action]()

            # ==========================================
            # Windows Applications
            # ==========================================

            windows_actions = {

                "OPEN_NOTEPAD": WindowsAutomation.open_notepad,
                "OPEN_CALCULATOR": WindowsAutomation.open_calculator,
                "OPEN_PAINT": WindowsAutomation.open_paint,
                "OPEN_CMD": WindowsAutomation.open_cmd,
                "OPEN_EXPLORER": WindowsAutomation.open_explorer,

            }

            if action in windows_actions:

                JarvisLogger.info(
                    f"Executing : {action}"
                )

                return windows_actions[action]()

            # ==========================================
            # File Manager
            # ==========================================

            file_actions = {

                "OPEN_DESKTOP": FileManager.open_desktop,
                "OPEN_DOWNLOADS": FileManager.open_downloads,
                "OPEN_DOCUMENTS": FileManager.open_documents,

            }

            if action in file_actions:

                JarvisLogger.info(
                    f"Executing : {action}"
                )

                return file_actions[action]()

            # ==========================================
            # Camera / System
            # ==========================================

            system_actions = {

                "OPEN_CAMERA": CameraAutomation.open_camera,
                "TAKE_PHOTO": CameraAutomation.take_photo,

                "TAKE_SCREENSHOT": SystemControl.take_screenshot,

                "LOCK_PC": SystemControl.lock_pc,

                "VOLUME_UP": SystemControl.volume_up,
                "VOLUME_DOWN": SystemControl.volume_down,
                "MUTE_VOLUME": SystemControl.mute_volume,

            }

            if action in system_actions:

                JarvisLogger.info(
                    f"Executing : {action}"
                )

                return system_actions[action]()

            # ==========================================
            # System Information
            # ==========================================

            info_actions = {

                "GET_BATTERY": SystemInfo.get_battery,
                "GET_CPU": SystemInfo.get_cpu,
                "GET_RAM": SystemInfo.get_ram,
                "GET_DISK": SystemInfo.get_disk,

            }

            if action in info_actions:

                JarvisLogger.info(
                    f"Executing : {action}"
                )

                return info_actions[action]()

            # ==========================================
            # Time & Date
            # ==========================================

            if action == "GET_TIME":

                return datetime.now().strftime(
                    "Current time is %I:%M %p"
                )

            if action == "GET_DATE":

                return datetime.now().strftime(
                    "Today is %d %B %Y"
                )

            # ==========================================
            # Greetings
            # ==========================================

            if action == "INTRO":

                return (
                    "Hello Krishna. I am Jarvis, your personal AI assistant. "
                    "I can open applications, search files, control your computer, "
                    "answer questions using AI, remember information, manage reminders "
                    "and much more."
                )

            if action == "GREET":

                hour = datetime.now().hour

                if hour < 12:
                    return "Good morning Krishna."

                elif hour < 17:
                    return "Good afternoon Krishna."

                elif hour < 21:
                    return "Good evening Krishna."

                return "Hello Krishna."

            # ==========================================
            # Unknown Action
            # ==========================================

            JarvisLogger.warning(
                f"Unknown Action : {action}"
            )

            return (
                "Sorry Krishna, I don't know how to perform that action yet."
            )

        except Exception as e:

            JarvisLogger.error(
                f"Command Router Error : {e}"
            )

            return (
                "Sorry Krishna, something went wrong while executing the command."
            )