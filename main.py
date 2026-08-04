import threading
import traceback

from core.assistant import JarvisAssistant
from core.logger import JarvisLogger

from gui.controller import GUIController


def start_assistant():
    """
    Start Jarvis Assistant in background thread.
    """

    try:

        JarvisLogger.success(
            "Starting Assistant Thread..."
        )

        assistant = JarvisAssistant()

        assistant.start()

    except Exception as e:

        JarvisLogger.critical(
            f"Assistant crashed : {e}"
        )

        traceback.print_exc()


def main():

    try:

        JarvisLogger.success(
            "Launching GUI..."
        )

        GUIController.create()

        assistant_thread = threading.Thread(
            target=start_assistant,
            daemon=True,
            name="JarvisAssistant"
        )

        assistant_thread.start()

        GUIController.run()

    except KeyboardInterrupt:

        JarvisLogger.warning(
            "Program interrupted by user."
        )

    except Exception as e:

        JarvisLogger.critical(
            f"Fatal Error : {e}"
        )

        traceback.print_exc()


if __name__ == "__main__":
    main()