import os

DATA_DIR_NAME = '.umbrella'
LOGS_DIR_NAME = 'logs'
HOME_DIR_SIGN = '~'


def home() -> str:
    return os.path.expanduser(HOME_DIR_SIGN)


def current_dir() -> str:
    return os.path.abspath(os.curdir)


def date_dir() -> str:
    return f'{home()}/{DATA_DIR_NAME}'


def logs_dir() -> str:
    return f'{date_dir()}/{LOGS_DIR_NAME}'


def check_file_exists(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
