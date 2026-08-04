import os
import shutil
import subprocess

from core.logger import JarvisLogger


class FileManager:

    # ======================================

    @staticmethod
    def _open_folder(path, name):

        try:

            if not os.path.exists(path):

                return f"{name} folder does not exist."

            subprocess.Popen(
                ["explorer", path]
            )

            JarvisLogger.success(
                f"{name} opened."
            )

            return f"Opening {name}."

        except Exception as e:

            JarvisLogger.error(
                f"{name} Error : {e}"
            )

            return f"Unable to open {name}."

    # ======================================

    @staticmethod
    def open_desktop():

        path = os.path.join(
            os.path.expanduser("~"),
            "Desktop"
        )

        return FileManager._open_folder(
            path,
            "Desktop"
        )

    # ======================================

    @staticmethod
    def open_downloads():

        path = os.path.join(
            os.path.expanduser("~"),
            "Downloads"
        )

        return FileManager._open_folder(
            path,
            "Downloads"
        )

    # ======================================

    @staticmethod
    def open_documents():

        path = os.path.join(
            os.path.expanduser("~"),
            "Documents"
        )

        return FileManager._open_folder(
            path,
            "Documents"
        )

    # ======================================

    @staticmethod
    def create_folder(folder_name):

        try:

            path = os.path.join(
                os.getcwd(),
                folder_name
            )

            os.makedirs(
                path,
                exist_ok=True
            )

            JarvisLogger.success(
                f"Folder Created : {folder_name}"
            )

            return f"Folder '{folder_name}' created."

        except Exception as e:

            JarvisLogger.error(
                f"Create Folder Error : {e}"
            )

            return "Unable to create folder."

    # ======================================

    @staticmethod
    def delete_folder(folder_name):

        try:

            path = os.path.join(
                os.getcwd(),
                folder_name
            )

            if not os.path.exists(path):

                return f"Folder '{folder_name}' does not exist."

            shutil.rmtree(path)

            JarvisLogger.success(
                f"Folder Deleted : {folder_name}"
            )

            return f"Folder '{folder_name}' deleted."

        except Exception as e:

            JarvisLogger.error(
                f"Delete Folder Error : {e}"
            )

            return "Unable to delete folder."

    # ======================================

    @staticmethod
    def create_file(file_name):

        try:

            path = os.path.join(
                os.getcwd(),
                file_name
            )

            with open(
                path,
                "w",
                encoding="utf-8"
            ):
                pass

            JarvisLogger.success(
                f"File Created : {file_name}"
            )

            return f"File '{file_name}' created."

        except Exception as e:

            JarvisLogger.error(
                f"Create File Error : {e}"
            )

            return "Unable to create file."

    # ======================================

    @staticmethod
    def delete_file(file_name):

        try:

            path = os.path.join(
                os.getcwd(),
                file_name
            )

            if not os.path.exists(path):

                return f"File '{file_name}' does not exist."

            os.remove(path)

            JarvisLogger.success(
                f"File Deleted : {file_name}"
            )

            return f"File '{file_name}' deleted."

        except Exception as e:

            JarvisLogger.error(
                f"Delete File Error : {e}"
            )

            return "Unable to delete file."