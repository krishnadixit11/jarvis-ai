import os
import string
import subprocess

from core.logger import JarvisLogger


class FileSearch:

    @staticmethod
    def get_drives():
        drives = []

        for letter in string.ascii_uppercase:
            drive = f"{letter}:\\"

            if os.path.exists(drive):
                drives.append(drive)

        return drives

    @staticmethod
    def search_file(name):

        JarvisLogger.info(
            f"Searching file: {name}"
        )

        results = []

        for drive in FileSearch.get_drives():

            for root, dirs, files in os.walk(
                drive,
                topdown=True,
                onerror=lambda e: None
            ):

                try:

                    for file in files:

                        if name.lower() in file.lower():

                            path = os.path.join(
                                root,
                                file
                            )

                            results.append(path)

                            if len(results) >= 5:
                                break

                    if len(results) >= 5:
                        break

                except PermissionError:
                    continue

            if len(results) >= 5:
                break

        if results:

            message = "Found files:\n\n"

            for i, path in enumerate(results, 1):
                message += f"{i}. {path}\n"

            return message

        return "File not found."

    @staticmethod
    def open_file(path):

        if os.path.exists(path):

            os.startfile(path)

            return "Opening file."

        return "File does not exist."

    @staticmethod
    def open_folder(path):

        if os.path.exists(path):

            subprocess.Popen(
                f'explorer "{path}"'
            )

            return "Opening folder."

        return "Folder does not exist."