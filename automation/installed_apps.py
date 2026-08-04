import os

from core.logger import JarvisLogger


class InstalledApps:

    _cache = None

    @classmethod
    def get_shortcuts(cls):

        # ==============================
        # Return Cache
        # ==============================

        if cls._cache is not None:
            return cls._cache

        shortcuts = {}

        folders = []

        try:

            program_data = os.environ.get("PROGRAMDATA")

            if program_data:

                folders.append(
                    os.path.join(
                        program_data,
                        r"Microsoft\Windows\Start Menu\Programs"
                    )
                )

        except Exception:
            pass

        try:

            app_data = os.environ.get("APPDATA")

            if app_data:

                folders.append(
                    os.path.join(
                        app_data,
                        r"Microsoft\Windows\Start Menu\Programs"
                    )
                )

        except Exception:
            pass

        # ==============================
        # Scan Shortcuts
        # ==============================

        for folder in folders:

            if not os.path.exists(folder):
                continue

            for root, _, files in os.walk(folder):

                for file in files:

                    try:

                        if not file.lower().endswith(".lnk"):
                            continue

                        name = os.path.splitext(file)[0].lower().strip()

                        path = os.path.join(root, file)

                        # Duplicate ignore
                        if name not in shortcuts:
                            shortcuts[name] = path

                    except Exception:
                        continue

        cls._cache = shortcuts

        JarvisLogger.success(
            f"Installed Apps Loaded : {len(shortcuts)}"
        )

        return shortcuts