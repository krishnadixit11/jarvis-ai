import sqlite3

from core.logger import JarvisLogger


class Memory:

    def __init__(self):

        self.connection = sqlite3.connect(
            "database/sqlite.db"
        )

        self.cursor = self.connection.cursor()

        self.create_table()


    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE,
            value TEXT
        )
        """)

        self.connection.commit()


    def remember(self, key, value):

        self.cursor.execute(
            """
            INSERT OR REPLACE INTO memory(key,value)
            VALUES(?,?)
            """,
            (key, value)
        )

        self.connection.commit()

        JarvisLogger.info(
            f"Memory saved: {key} = {value}"
        )

        return "I will remember that."


    def recall(self, key):

        self.cursor.execute(
            """
            SELECT value FROM memory
            WHERE key=?
            """,
            (key,)
        )

        result = self.cursor.fetchone()

        if result:
            return result[0]

        return None