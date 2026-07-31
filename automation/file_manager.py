import os
import subprocess

from core.logger import JarvisLogger


class FileManager:

    @staticmethod
    def open_desktop():
        path = os.path.join(os.path.expanduser("~"), "Desktop")
        JarvisLogger.info("Opening Desktop")
        subprocess.Popen(f'explorer "{path}"')
        return "Opening Desktop."

    @staticmethod
    def open_downloads():
        path = os.path.join(os.path.expanduser("~"), "Downloads")
        JarvisLogger.info("Opening Downloads")
        subprocess.Popen(f'explorer "{path}"')
        return "Opening Downloads."

    @staticmethod
    def open_documents():
        path = os.path.join(os.path.expanduser("~"), "Documents")
        JarvisLogger.info("Opening Documents")
        subprocess.Popen(f'explorer "{path}"')
        return "Opening Documents."

    @staticmethod
    def create_folder(folder_name):
        path = os.path.join(os.getcwd(), folder_name)

        if not os.path.exists(path):
            os.makedirs(path)
            JarvisLogger.info(f"Folder Created: {folder_name}")
            return f"Folder {folder_name} created successfully."

        return f"Folder {folder_name} already exists."

    @staticmethod
    def delete_folder(folder_name):
        path = os.path.join(os.getcwd(), folder_name)

        if os.path.exists(path):
            os.rmdir(path)
            JarvisLogger.info(f"Folder Deleted: {folder_name}")
            return f"Folder {folder_name} deleted successfully."

        return f"Folder {folder_name} does not exist."

    @staticmethod
    def create_file(file_name):
        path = os.path.join(os.getcwd(), file_name)

        with open(path, "w", encoding="utf-8") as file:
            file.write("")

        JarvisLogger.info(f"File Created: {file_name}")

        return f"File {file_name} created successfully."

    @staticmethod
    def delete_file(file_name):
        path = os.path.join(os.getcwd(), file_name)

        if os.path.exists(path):
            os.remove(path)
            JarvisLogger.info(f"File Deleted: {file_name}")
            return f"File {file_name} deleted successfully."

        return f"File {file_name} does not exist."
