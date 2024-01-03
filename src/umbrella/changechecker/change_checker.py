from abc import ABC, abstractmethod


class ChangeChecker(ABC):
    @abstractmethod
    def is_changed(self, folder_path: str) -> bool:
        """ Checks the folder for any content changes"""
        pass


class MD5ChangeChecker(ChangeChecker):
    def is_changed(self, folder_path: str) -> bool:
        """ Checks the folder for any content changes by comparison its MD5 checksum"""
        # TODO Not implemented yet
        return True