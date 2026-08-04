import os
import string
import subprocess

from core.logger import JarvisLogger


class FileSearch:

    MAX_RESULTS = 10

    # =====================================

    @staticmethod
    def get_drives():

        drives = []

        for letter in string.ascii_uppercase:

            drive = f"{letter}:\\"

            if os.path.exists(drive):
                drives.append(drive)

        return drives

    # =====================================

    @staticmethod
    def search_file(name):

        name = name.strip().lower()

        if not name:
            return "Please tell me which file you want to search."

        JarvisLogger.info(
            f"Searching File : {name}"
        )

        results = []

        try:

            for drive in FileSearch.get_drives():

                for root, dirs, files in os.walk(
                    drive,
                    topdown=True,
                    followlinks=False
                ):

                    # Skip hidden/system folders
                    dirs[:] = [
                        d for d in dirs
                        if not d.startswith("$")
                    ]

                    try:

                        for file in files:

                            if name in file.lower():

                                path = os.path.join(root, file)

                                results.append(path)

                                if len(results) >= FileSearch.MAX_RESULTS:
                                    break

                    except (
                        PermissionError,
                        FileNotFoundError,
                        OSError
                    ):
                        continue

                    if len(results) >= FileSearch.MAX_RESULTS:
                        break

                if len(results) >= FileSearch.MAX_RESULTS:
                    break

        except Exception as e:

            JarvisLogger.error(
                f"Search Error : {e}"
            )

            return "Something went wrong while searching."

        if not results:
            return f"No file found named '{name}'."

        message = "I found these files:\n\n"

        for index, path in enumerate(results, start=1):

            message += f"{index}. {path}\n"

        return message

    # =====================================

    @staticmethod
    def search_folder(name):

        name = name.strip().lower()

        if not name:
            return "Please tell me which folder you want to search."

        JarvisLogger.info(
            f"Searching Folder : {name}"
        )

        results = []

        try:

            for drive in FileSearch.get_drives():

                for root, dirs, files in os.walk(
                    drive,
                    topdown=True,
                    followlinks=False
                ):

                    try:

                        for folder in dirs:

                            if name in folder.lower():

                                path = os.path.join(root, folder)

                                results.append(path)

                                if len(results) >= FileSearch.MAX_RESULTS:
                                    break

                    except (
                        PermissionError,
                        FileNotFoundError,
                        OSError
                    ):
                        continue

                    if len(results) >= FileSearch.MAX_RESULTS:
                        break

                if len(results) >= FileSearch.MAX_RESULTS:
                    break

        except Exception as e:

            JarvisLogger.error(
                f"Folder Search Error : {e}"
            )

            return "Something went wrong while searching."

        if not results:
            return f"No folder found named '{name}'."

        message = "I found these folders:\n\n"

        for index, path in enumerate(results, start=1):

            message += f"{index}. {path}\n"

        return message

    # =====================================

    @staticmethod
    def open_file(path):

        if not path:
            return "Invalid file."

        if not os.path.isfile(path):
            return "File does not exist."

        try:

            JarvisLogger.info(
                f"Opening File : {path}"
            )

            os.startfile(path)

            return "Opening file."

        except Exception as e:

            JarvisLogger.error(
                f"Open File Error : {e}"
            )

            return "Unable to open file."

    # =====================================

    @staticmethod
    def open_folder(path):

        if not path:
            return "Invalid folder."

        if not os.path.isdir(path):
            return "Folder does not exist."

        try:

            JarvisLogger.info(
                f"Opening Folder : {path}"
            )

            subprocess.Popen(
                ["explorer", path]
            )

            return "Opening folder."

        except Exception as e:

            JarvisLogger.error(
                f"Open Folder Error : {e}"
            )

            return "Unable to open folder."