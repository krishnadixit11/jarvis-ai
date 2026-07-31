import threading
import time
from datetime import datetime

from core.logger import JarvisLogger


class AlarmManager:

    alarms = []
    reminders = []

    @staticmethod
    def set_alarm(alarm_time):

        def alarm_thread():

            JarvisLogger.info(f"Alarm set for {alarm_time}")

            while True:

                now = datetime.now().strftime("%H:%M")

                if now == alarm_time:

                    print("\n")
                    print("=" * 50)
                    print("🔔 ALARM! TIME'S UP!")
                    print("=" * 50)

                    try:
                        import winsound

                        for _ in range(8):
                            winsound.Beep(1000, 700)

                    except Exception:
                        pass

                    break

                time.sleep(20)

        threading.Thread(
            target=alarm_thread,
            daemon=True
        ).start()

        return f"Alarm set for {alarm_time}."


    @staticmethod
    def set_reminder(reminder_time, message):

        def reminder_thread():

            JarvisLogger.info(
                f"Reminder set for {reminder_time}"
            )

            while True:

                now = datetime.now().strftime("%H:%M")

                if now == reminder_time:

                    print("\n")
                    print("=" * 50)
                    print(f"📌 REMINDER : {message}")
                    print("=" * 50)

                    try:
                        import winsound

                        winsound.Beep(900, 600)

                    except Exception:
                        pass

                    break

                time.sleep(20)

        threading.Thread(
            target=reminder_thread,
            daemon=True
        ).start()

        return f"Reminder set for {reminder_time}."