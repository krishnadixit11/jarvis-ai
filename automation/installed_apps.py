import os


class InstalledApps:

    @staticmethod
    def get_shortcuts():

        folders = [

            os.path.join(
                os.environ["PROGRAMDATA"],
                r"Microsoft\Windows\Start Menu\Programs"
            ),

            os.path.join(
                os.environ["APPDATA"],
                r"Microsoft\Windows\Start Menu\Programs"
            ),

        ]

        shortcuts = {}

        for folder in folders:

            if not os.path.exists(folder):
                continue

            for root, dirs, files in os.walk(folder):

                for file in files:

                    if file.endswith(".lnk"):

                        name = file.replace(".lnk", "").lower()

                        shortcuts[name] = os.path.join(
                            root,
                            file
                        )

        return shortcuts