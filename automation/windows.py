import subprocess

from core.logger import JarvisLogger


class WindowsAutomation:

    # =====================================
    # Internal App Launcher
    # =====================================

    @staticmethod
    def _launch(command, app_name):

        try:

            JarvisLogger.info(
                f"Opening {app_name}..."
            )

            subprocess.Popen(
                command,
                shell=True
            )

            JarvisLogger.success(
                f"{app_name} opened successfully."
            )

            return f"Opening {app_name}."

        except FileNotFoundError:

            JarvisLogger.error(
                f"{app_name} not found."
            )

            return f"{app_name} is not installed."

        except Exception as e:

            JarvisLogger.error(
                f"{app_name} Error : {e}"
            )

            return f"Unable to open {app_name}."

    # =====================================
    # Windows Applications
    # =====================================

    @staticmethod
    def open_notepad():

        return WindowsAutomation._launch(
            "notepad.exe",
            "Notepad"
        )

    @staticmethod
    def open_calculator():

        return WindowsAutomation._launch(
            "calc.exe",
            "Calculator"
        )

    @staticmethod
    def open_paint():

        return WindowsAutomation._launch(
            "mspaint.exe",
            "Paint"
        )

    @staticmethod
    def open_cmd():

        return WindowsAutomation._launch(
            "cmd.exe",
            "Command Prompt"
        )

    @staticmethod
    def open_explorer():

        return WindowsAutomation._launch(
            "explorer.exe",
            "File Explorer"
        )

    # =====================================
    # Extra Windows Apps
    # =====================================

    @staticmethod
    def open_task_manager():

        return WindowsAutomation._launch(
            "taskmgr.exe",
            "Task Manager"
        )

    @staticmethod
    def open_registry():

        return WindowsAutomation._launch(
            "regedit.exe",
            "Registry Editor"
        )

    @staticmethod
    def open_control_panel():

        return WindowsAutomation._launch(
            "control.exe",
            "Control Panel"
        )

    @staticmethod
    def open_settings():

        return WindowsAutomation._launch(
            "start ms-settings:",
            "Windows Settings"
        )

    @staticmethod
    def open_device_manager():

        return WindowsAutomation._launch(
            "devmgmt.msc",
            "Device Manager"
        )

    @staticmethod
    def open_services():

        return WindowsAutomation._launch(
            "services.msc",
            "Services"
        )

    @staticmethod
    def open_run():

        return WindowsAutomation._launch(
            "explorer.exe shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}",
            "Run Dialog"
        )