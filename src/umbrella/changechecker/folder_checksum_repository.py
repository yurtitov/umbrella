import sqlite3

from abc import ABC, abstractmethod

DB_NAME = 'umbrella.db'


class FolderChecksumRepository(ABC):
    @abstractmethod
    def get_checksum(self, folder_path: str) -> str | None:
        pass

    @abstractmethod
    def set_checksum(self, folder_path: str, checksum: str):
        pass


class SqliteFolderChecksumRepository(FolderChecksumRepository):
    def __init__(self, db_name=None):
        if db_name is None:
            self.__db_name = DB_NAME
        else:
            self.__db_name = db_name
        self.__init_db()

    def get_checksum(self, folder_path: str) -> str | None:
        return self.__get_checksum(folder_path)

    def set_checksum(self, folder_path: str, checksum: str):
        if self.__is_exist(folder_path):
            self.__update(folder=folder_path, checksum=checksum)
        else:
            self.__insert(folder=folder_path, checksum=checksum)

    def __init_db(self):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Checksums (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        folder TEXT NOT NULL UNIQUE,
        checksum TEXT NOT NULL UNIQUE
        )
        """)
        connection.commit()
        connection.close()

    def __insert(self, folder: str, checksum: str):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Checksums (folder, checksum) VALUES (?, ?, ?)', (folder, checksum))
        connection.commit()
        connection.close()

    def __update(self, folder: str, checksum: str):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute('UPDATE Checksums SET checksum = ? WHERE folder = ?', (checksum, folder))
        connection.commit()
        connection.close()

    def __delete(self, folder: str):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Checksums WHERE folder = ?', (folder,))
        connection.commit()
        connection.close()

    def __get_checksum(self, folder: str) -> str | None:
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute('SELECT checksum FROM Checksums WHERE folder = ?', (folder,))
        checksum = cursor.fetchone()
        connection.close()
        return checksum

    def __is_exist(self, folder_path) -> bool:
        return self.__get_checksum(folder_path) is not None
