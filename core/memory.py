import os
import sqlite3

from core.logger import JarvisLogger


class Memory:

    def __init__(self):

        os.makedirs("database", exist_ok=True)

        self.connection = sqlite3.connect(
            "database/sqlite.db",
            check_same_thread=False
        )

        self.connection.execute(
            "PRAGMA journal_mode=WAL"
        )

        self.connection.execute(
            "PRAGMA synchronous=NORMAL"
        )

        self.cursor = self.connection.cursor()

        self.create_table()

    # =====================================================

    def create_table(self):

        try:

            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS memory(

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    key TEXT UNIQUE NOT NULL,

                    value TEXT NOT NULL

                )
                """
            )

            self.connection.commit()

        except Exception as e:

            JarvisLogger.error(
                f"Memory Table Error : {e}"
            )

    # =====================================================

    def remember(self, key, value):

        key = key.lower().strip()

        value = value.strip()

        try:

            self.cursor.execute(

                """
                INSERT INTO memory(key,value)

                VALUES(?,?)

                ON CONFLICT(key)

                DO UPDATE SET value=excluded.value
                """,

                (
                    key,
                    value
                )

            )

            self.connection.commit()

            JarvisLogger.success(
                f"Memory Saved : {key} = {value}"
            )

            return "I will remember that."

        except Exception as e:

            JarvisLogger.error(
                f"Remember Error : {e}"
            )

            return "Unable to save memory."

    # =====================================================

    def recall(self, key):

        key = key.lower().strip()

        try:

            self.cursor.execute(

                """
                SELECT value

                FROM memory

                WHERE key=?
                """,

                (key,)

            )

            result = self.cursor.fetchone()

            if result:

                return result[0]

            return None

        except Exception as e:

            JarvisLogger.error(
                f"Recall Error : {e}"
            )

            return None

    # =====================================================

    def forget(self, key):

        key = key.lower().strip()

        try:

            self.cursor.execute(

                """
                DELETE FROM memory

                WHERE key=?
                """,

                (key,)

            )

            self.connection.commit()

            if self.cursor.rowcount:

                return "Memory deleted."

            return "Memory not found."

        except Exception as e:

            JarvisLogger.error(
                f"Forget Error : {e}"
            )

            return "Unable to delete memory."

    # =====================================================

    def get_all(self):

        try:

            self.cursor.execute(

                """
                SELECT key,value

                FROM memory

                ORDER BY key
                """

            )

            return self.cursor.fetchall()

        except Exception as e:

            JarvisLogger.error(
                f"Memory Read Error : {e}"
            )

            return []

    # =====================================================

    def close(self):

        try:

            self.connection.close()

        except Exception:

            pass

    # =====================================================

    def __del__(self):

        self.close()