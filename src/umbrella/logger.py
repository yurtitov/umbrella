import logging
from path_utils import logs_dir


class CommonLogger:

    def __init__(self, logger_name: str, log_file_name: str, level: int = logging.DEBUG):
        self.__logger = logging.getLogger(logger_name)
        self.__logger.setLevel(level)
        self.__formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
        self.__handler = logging.FileHandler(filename=log_file_name, encoding='utf-8')
        self.__handler.setLevel(level)
        self.__handler.setFormatter(self.__formatter)
        self.__logger.addHandler(self.__handler)

    def get_logger(self):
        return self.__logger


class MainLogger(CommonLogger):
    def __init__(self, logger_name: str = 'AppLogger', log_file_name: str = 'app.log'):
        full_path = f'{logs_dir()}/{log_file_name}'
        super().__init__(logger_name, full_path)


class ActionLogger(CommonLogger):
    def __init__(self, logger_name: str = 'ActionLogger', log_file_name: str = 'action.log'):
        full_path = f'{logs_dir()}/{log_file_name}'
        super().__init__(logger_name, full_path)
