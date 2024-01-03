#!/usr/bin/python3

import subprocess
import sys
from path_utils import is_dir
from subprocess import CalledProcessError
from datetime import datetime

from logger import ActionLogger
from changechecker.change_checker import ChangeChecker, MD5ChangeChecker


class GitBackupAction:
    def __init__(self, target_folder_path: str, folder_change_checker: ChangeChecker):
        assert is_dir(target_folder_path)
        self.__target_folder_path = target_folder_path
        self.__logger = ActionLogger().get_logger()
        self.__folder_change_checker = folder_change_checker

    def run(self):
        self.__logger.info('Action script started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        script_lines = self.__get_script(self.__target_folder_path)
        self.__logger.info(f'Target path: {self.__target_folder_path}')
        for line in script_lines:
            try:
                process = subprocess.Popen(
                    line,
                    shell=True,
                    executable="/bin/bash",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT
                )
                process_output, process_error = process.communicate()
                self.__log_process_output(str(process_output))

            except (OSError, CalledProcessError) as exception:
                self.__logger.info(f'Exception occurred: {str(exception)}. Subprocess failed.')
            else:
                self.__logger.info('Action script finished <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    def __get_script(self, __target_path) -> list[str]:
        result: list[str] = []
        if self.__folder_change_checker.is_changed(self.__target_folder_path):
            now = datetime.now().strftime("%Y%m%d, %H:%M")
            result.append(
                f'cd {__target_path} && git pull && git add -A && git commit -m "Automatic commit: {now}" && git push')
        else:
            result.append(f'echo "Content has not changed for path: {__target_path}"')
        return result

    def __log_process_output(self, process_output: str):
        process_output = process_output[2:-1]
        lines = process_output.split('\\n')
        for line in lines:
            self.__logger.info(line)


if __name__ == '__main__':
    target_path = sys.argv[1:][0]
    action = GitBackupAction(target_path, MD5ChangeChecker())
    action.run()
