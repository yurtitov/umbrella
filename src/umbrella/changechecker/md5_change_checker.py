from abstract_change_checker import ChangeChecker
from folder_checksum_repository import FolderChecksumRepository
from pathlib import Path
from checksumdir import dirhash


class MD5ChangeChecker(ChangeChecker):
    def __init__(self, folder_checksum_repo: FolderChecksumRepository):
        self.__folder_checksum_repo = folder_checksum_repo

    def is_changed(self, folder_path: str) -> bool:
        """ Checks the folder for any content changes by comparison its MD5 checksum"""
        assert Path(folder_path).is_dir()
        current_md5 = self.__get_md5(folder_path)
        previous_md5 = self.__get_previous_md5(folder_path)
        self.__persist_md5(folder_path, current_md5)
        return current_md5 != previous_md5

    @staticmethod
    def __get_md5(folder_path) -> str:
        return dirhash(folder_path, hashfunc="md5")

    def __get_previous_md5(self, folder_path) -> str | None:
        return self.__folder_checksum_repo.get_checksum(folder_path)

    def __persist_md5(self, folder_path, current_md5):
        self.__folder_checksum_repo.set_checksum(folder_path=folder_path, checksum=current_md5)
