import os

DATA_DIR_NAME = '.umbrella'


def home() -> str:
    return os.path.expanduser('~')


def curdir() -> str:
    return os.path.abspath(os.curdir)


def datadir() -> str:
    return f'{home()}/{DATA_DIR_NAME}'
