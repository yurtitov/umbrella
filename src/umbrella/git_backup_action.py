#!/usr/bin/python3

import subprocess
import sys
import logging
import path_utils
from datetime import datetime


class GitBackupAction:
    def __init__(self, target: str):
        self.__target_path = target
        log_path = f'{path_utils.datadir()}/git-backup-action.log'
        print(log_path)
        logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.DEBUG)
        logging.info(f'GitBackupAction is created')

    def run(self):
        logging.info('Action run')
        script_lines = self.__get_script(self.__target_path)
        logging.info(f'Script: {script_lines}')
        for line in script_lines:
            output_file = f'{path_utils.datadir()}/bbb.log'
            with open(output_file, 'a') as file:
                subprocess.run(line, shell=True, executable="/bin/bash", stdout=file, stderr=file)

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


if __name__ == '__main__':
    target_path = sys.argv[1:]
    log_path = f'{path_utils.datadir()}/action.log'
    logging.basicConfig(filename=log_path)
    logging.info(f'Target: {target_path}')
    action = GitBackupAction(target_path[0])
    action.run()
