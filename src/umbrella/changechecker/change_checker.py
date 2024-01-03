from abc import ABC, abstractmethod
from pathlib import Path


class ChangeChecker(ABC):
    @abstractmethod
    def is_changed(self, folder_path: str) -> bool:
        """ Checks the folder for any content changes"""
        pass


class MD5ChangeChecker(ChangeChecker):
    def is_changed(self, folder_path: str) -> bool:
        """ Checks the folder for any content changes by comparison its MD5 checksum"""
        assert Path(folder_path).is_dir()
        current_md5 = self.__get_folder_md5(folder_path)
        previous_md5 = self.__get_previous_folder_md5(folder_path)
        return current_md5 != previous_md5

    def __get_folder_md5(self, folder_path) -> str:
        # TODO Not implemented yet
        return ""

    def __get_previous_folder_md5(self, folder_path) -> str:
        # TODO Not implemented yet
        return ""