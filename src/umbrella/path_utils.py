import os

DATA_DIR_NAME = '.umbrella'
LOGS_DIR_NAME = 'logs'
HOME_DIR_SIGN = '~'


def home_dir() -> str:
    return os.path.expanduser(HOME_DIR_SIGN)


def current_dir() -> str:
    return os.path.abspath(os.curdir)


def data_dir() -> str:
    return f'{home_dir()}/{DATA_DIR_NAME}'


def logs_dir() -> str:
    return f'{data_dir()}/{LOGS_DIR_NAME}'


def is_dir(path: str) -> bool:
    return os.path.isdir(path)


def is_file(path: str) -> bool:
    return os.path.isfile(path)


def check_file_exists(file_path):
    if not is_file(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
