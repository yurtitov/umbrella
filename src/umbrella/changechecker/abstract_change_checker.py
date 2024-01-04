from abc import ABC, abstractmethod


class ChangeChecker(ABC):
    @abstractmethod
    def is_changed(self, folder_path: str) -> bool:
        """ Checks the folder for any content changes"""
        pass
