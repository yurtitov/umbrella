#!/usr/bin/python3

import subprocess
import sys
from subprocess import CalledProcessError
from datetime import datetime

from logger import ActionLogger


class GitBackupAction:
    def __init__(self, target: str):
        self.__target_path = target
        self.__logger = ActionLogger().get_logger()

    def run(self):
        self.__logger.info('Action script started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        script_lines = self.__get_script(self.__target_path)
        self.__logger.info(f'Target path: {self.__target_path}')
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
                self.__logger.info(f'Exception occured: {str(exception)}. Subprocess failed.')
            else:
                self.__logger.info('Action script finished <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    def __get_script(self, __target_path) -> list[str]:
        result: list[str] = []
        if self.__content_changed(__target_path):
            now = datetime.now().strftime("%Y%m%d, %H:%M")
            result.append(
                f'cd {__target_path} && git pull && git add -A && git commit -m "Automatic commit: {now}" && git push')
        else:
            result.append(f'echo "Content has not changed for path: {__target_path}"')
        return result

    def __content_changed(self, __target_path):
        return True

    def __log_process_output(self, process_output: str):
        process_output = process_output[2:-1]
        lines = process_output.split('\\n')
        for line in lines:
            self.__logger.info(line)


if __name__ == '__main__':
    target_path = sys.argv[1:]
    action = GitBackupAction(target_path[0])
    action.run()
