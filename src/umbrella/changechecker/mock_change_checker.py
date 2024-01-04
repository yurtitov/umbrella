from abstract_change_checker import ChangeChecker


class MockChangeChecker(ChangeChecker):
    def is_changed(self, folder_path: str) -> bool:
        return True
