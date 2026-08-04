import os
import platform
import psutil

from core.logger import JarvisLogger


class SystemInfo:

    # ==========================================
    # Battery
    # ==========================================

    @staticmethod
    def get_battery():

        try:

            battery = psutil.sensors_battery()

            if battery is None:
                return "Battery information is not available."

            percent = int(battery.percent)

            if battery.power_plugged:
                return f"Battery is {percent}% and charging."

            if percent >= 80:
                status = "Battery is excellent."

            elif percent >= 50:
                status = "Battery level is good."

            elif percent >= 20:
                status = "Battery is getting low."

            else:
                status = "Battery is critically low."

            return f"{status} Current battery is {percent}%."

        except Exception as e:

            JarvisLogger.error(
                f"Battery Error : {e}"
            )

            return "Unable to read battery status."

    # ==========================================
    # CPU
    # ==========================================

    @staticmethod
    def get_cpu():

        try:

            usage = psutil.cpu_percent(interval=0.5)

            cores = psutil.cpu_count(logical=True)

            return (
                f"CPU usage is {usage}% "
                f"across {cores} logical cores."
            )

        except Exception as e:

            JarvisLogger.error(
                f"CPU Error : {e}"
            )

            return "Unable to read CPU usage."

    # ==========================================
    # RAM
    # ==========================================

    @staticmethod
    def get_ram():

        try:

            memory = psutil.virtual_memory()

            used = round(memory.used / (1024 ** 3), 2)

            total = round(memory.total / (1024 ** 3), 2)

            return (
                f"RAM usage is {memory.percent}%. "
                f"{used} GB used out of {total} GB."
            )

        except Exception as e:

            JarvisLogger.error(
                f"RAM Error : {e}"
            )

            return "Unable to read RAM usage."

    # ==========================================
    # Disk
    # ==========================================

    @staticmethod
    def get_disk():

        try:

            if platform.system() == "Windows":
                drive = os.environ.get("SystemDrive", "C:")
                path = drive + "\\"
            else:
                path = "/"

            disk = psutil.disk_usage(path)

            total = round(disk.total / (1024 ** 3), 2)

            used = round(disk.used / (1024 ** 3), 2)

            free = round(disk.free / (1024 ** 3), 2)

            return (
                f"Disk usage is {disk.percent}%. "
                f"{used} GB used, "
                f"{free} GB free, "
                f"Total {total} GB."
            )

        except Exception as e:

            JarvisLogger.error(
                f"Disk Error : {e}"
            )

            return "Unable to read disk usage."