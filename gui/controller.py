from threading import Lock

from core.logger import JarvisLogger
from gui.app import JarvisGUI


class GUIController:

    _instance = None
    _lock = Lock()

    # =====================================================
    # Create GUI (Singleton)
    # =====================================================

    @classmethod
    def create(cls):

        with cls._lock:

            if cls._instance is None:

                try:

                    cls._instance = JarvisGUI()

                    JarvisLogger.success(
                        "GUI Controller Created."
                    )

                except Exception as e:

                    JarvisLogger.error(
                        f"GUI Creation Error : {e}"
                    )

                    cls._instance = None

        return cls._instance

    # =====================================================
    # Get Instance
    # =====================================================

    @classmethod
    def get(cls):

        return cls._instance

    # =====================================================
    # Is Running
    # =====================================================

    @classmethod
    def is_created(cls):

        return cls._instance is not None

    # =====================================================
    # Run GUI
    # =====================================================

    @classmethod
    def run(cls):

        if cls._instance is None:

            cls.create()

        try:

            JarvisLogger.info(
                "Launching GUI..."
            )

            cls._instance.run()

        except Exception as e:

            JarvisLogger.error(
                f"GUI Runtime Error : {e}"
            )

    # =====================================================
    # Restart GUI
    # =====================================================

    @classmethod
    def restart(cls):

        try:

            cls._instance = None

            JarvisLogger.info(
                "Restarting GUI..."
            )

            cls.create()

            cls.run()

        except Exception as e:

            JarvisLogger.error(
                f"GUI Restart Error : {e}"
            )

    # =====================================================
    # Destroy GUI
    # =====================================================

    @classmethod
    def destroy(cls):

        if cls._instance:

            try:

                if hasattr(cls._instance, "dashboard"):

                    cls._instance.dashboard.close()

                cls._instance = None

                JarvisLogger.info(
                    "GUI Destroyed."
                )

            except Exception as e:

                JarvisLogger.error(
                    f"GUI Destroy Error : {e}"
                )