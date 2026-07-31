import os
import subprocess

from core.logger import JarvisLogger
from automation.installed_apps import InstalledApps


class AppLauncher:

    @staticmethod
    def open_app(app):

        app = app.lower().strip()

        JarvisLogger.info(
            f"Opening app: {app}"
        )

        apps = {

            # ==========================
            # Browsers
            # ==========================

            "chrome": "start chrome",
            "google chrome": "start chrome",

            "edge": "start msedge",

            "firefox": "start firefox",

            # ==========================
            # Development
            # ==========================

            "vscode": "code",
            "visual studio code": "code",

            "pycharm": "pycharm64",

            "android studio": "studio64",

            "git bash": "git-bash",

            "terminal": "start cmd",

            # ==========================
            # Windows Apps
            # ==========================

            "notepad": "notepad",

            "calculator": "calc",

            "paint": "mspaint",

            "explorer": "explorer",

            "file explorer": "explorer",

            "cmd": "start cmd",

            "command prompt": "start cmd",

            # ==========================
            # Microsoft Office
            # ==========================

            "word": "start winword",

            "excel": "start excel",

            "powerpoint": "start powerpnt",

            # ==========================
            # Communication
            # ==========================

            "whatsapp": "start whatsapp",

            "telegram": "start telegram",

            "discord": "start discord",

            # ==========================
            # Media
            # ==========================

            "spotify": "spotify",

            "vlc": "vlc",

            # ==========================
            # Gaming
            # ==========================

            "steam": "steam",
        }

        # ==========================
        # Hardcoded Apps
        # ==========================

        if app in apps:

            subprocess.Popen(
                apps[app],
                shell=True
            )

            return f"Opening {app}."

        # ==========================
        # Installed Apps Search
        # ==========================

        installed_apps = InstalledApps.get_shortcuts()

        for app_name, shortcut in installed_apps.items():

            if app in app_name:

                os.startfile(shortcut)

                return f"Opening {app_name}."

        # ==========================
        # Not Found
        # ==========================

        return f"I don't know how to open {app}." 