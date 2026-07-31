import psutil


class SystemInfo:


    @staticmethod
    def get_battery():

        battery = psutil.sensors_battery()

        if battery is None:
            return "Battery information is not available."


        percent = int(battery.percent)


        if battery.power_plugged:
            return f"Battery is {percent} percent and charging."


        return f"Battery is {percent} percent."



    @staticmethod
    def get_cpu():

        cpu = psutil.cpu_percent(
            interval=1
        )

        return f"CPU usage is {cpu} percent."



    @staticmethod
    def get_ram():

        ram = psutil.virtual_memory()

        return (
            f"RAM usage is {ram.percent} percent."
        )



    @staticmethod
    def get_disk():

        disk = psutil.disk_usage("/")

        return (
            f"Disk usage is {disk.percent} percent."
        )