import os
import subprocess

from core.logger import JarvisLogger
from automation.installed_apps import InstalledApps


class AppLauncher:

    # ======================================

    APPS = {

        # Browsers
        "chrome": "start chrome",
        "google chrome": "start chrome",
        "edge": "start msedge",
        "firefox": "start firefox",

        # Development
        "vscode": "code",
        "visual studio code": "code",
        "vs code": "code",

        "pycharm": "pycharm64",
        "android studio": "studio64",

        "git bash": "git-bash",

        "terminal": "start cmd",
        "cmd": "start cmd",
        "command prompt": "start cmd",

        # Windows
        "notepad": "notepad",
        "calculator": "calc",
        "calc": "calc",
        "paint": "mspaint",

        "explorer": "explorer",
        "file explorer": "explorer",

        # Office
        "word": "start winword",
        "excel": "start excel",
        "powerpoint": "start powerpnt",

        # Communication
        "telegram": "start telegram",
        "discord": "start discord",
        "whatsapp": "start whatsapp",

        # Media
        "spotify": "spotify",
        "vlc": "vlc",

        # Gaming
        "steam": "steam",

    }

    # ======================================

    ALIASES = {

        "note pad": "notepad",
        "nodepad": "notepad",
        "northpad": "notepad",
        "not pad": "notepad",

        "vs": "vscode",

        "calc": "calculator",

    }

    # ======================================

    @staticmethod
    def open_app(app):

        app = app.lower().strip()

        app = AppLauncher.ALIASES.get(
            app,
            app
        )

        JarvisLogger.info(
            f"Opening App : {app}"
        )

        # ----------------------------------

        if app in AppLauncher.APPS:

            try:

                subprocess.Popen(

                    AppLauncher.APPS[app],

                    shell=True

                )

                JarvisLogger.success(
                    f"{app} launched."
                )

                return f"Opening {app}."

            except Exception as e:

                JarvisLogger.error(
                    f"Launch Error : {e}"
                )

                return f"Unable to open {app}."

        # ----------------------------------
        # Installed Apps
        # ----------------------------------

        try:

            installed = InstalledApps.get_shortcuts()

            for name, shortcut in installed.items():

                if app in name.lower():

                    os.startfile(shortcut)

                    JarvisLogger.success(
                        f"{name} launched."
                    )

                    return f"Opening {name}."

        except Exception as e:

            JarvisLogger.error(
                f"Installed App Search Error : {e}"
            )

        # ----------------------------------

        JarvisLogger.warning(
            f"Unknown App : {app}"
        )

        return f"I couldn't find {app} on this computer."