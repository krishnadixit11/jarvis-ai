import threading
import time
from datetime import datetime

from core.logger import JarvisLogger


class AlarmManager:

    alarms = set()

    reminders = set()

    # ======================================

    @staticmethod
    def _valid_time(value):

        try:

            datetime.strptime(value, "%H:%M")

            return True

        except ValueError:

            return False

    # ======================================

    @staticmethod
    def set_alarm(alarm_time):

        if not AlarmManager._valid_time(alarm_time):

            return "Invalid time format. Use HH:MM."

        if alarm_time in AlarmManager.alarms:

            return f"Alarm for {alarm_time} already exists."

        AlarmManager.alarms.add(alarm_time)

        def alarm_thread():

            JarvisLogger.info(
                f"Alarm Scheduled : {alarm_time}"
            )

            while True:

                now = datetime.now().strftime("%H:%M")

                if now == alarm_time:

                    JarvisLogger.success(
                        "Alarm Triggered."
                    )

                    print("\n" + "=" * 45)
                    print("🔔 ALARM!")
                    print("=" * 45)

                    try:

                        import winsound

                        for _ in range(5):

                            winsound.Beep(1000, 500)

                            time.sleep(0.1)

                    except Exception as e:

                        JarvisLogger.error(
                            f"Alarm Sound Error : {e}"
                        )

                    AlarmManager.alarms.discard(
                        alarm_time
                    )

                    break

                time.sleep(1)

        threading.Thread(

            target=alarm_thread,

            daemon=True

        ).start()

        return f"Alarm set for {alarm_time}."

    # ======================================

    @staticmethod
    def set_reminder(reminder_time, message):

        if not AlarmManager._valid_time(reminder_time):

            return "Invalid time format. Use HH:MM."

        key = (reminder_time, message)

        if key in AlarmManager.reminders:

            return "Reminder already exists."

        AlarmManager.reminders.add(key)

        def reminder_thread():

            JarvisLogger.info(
                f"Reminder Scheduled : {reminder_time}"
            )

            while True:

                now = datetime.now().strftime("%H:%M")

                if now == reminder_time:

                    JarvisLogger.success(
                        "Reminder Triggered."
                    )

                    print("\n" + "=" * 45)
                    print(f"📌 REMINDER")
                    print(f"{message}")
                    print("=" * 45)

                    try:

                        import winsound

                        winsound.Beep(850, 600)

                    except Exception as e:

                        JarvisLogger.error(
                            f"Reminder Sound Error : {e}"
                        )

                    AlarmManager.reminders.discard(
                        key
                    )

                    break

                time.sleep(1)

        threading.Thread(

            target=reminder_thread,

            daemon=True

        ).start()

        return f"Reminder set for {reminder_time}."