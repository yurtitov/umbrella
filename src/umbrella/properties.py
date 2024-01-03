from logging import Logger

import yaml
import path_utils

from logger import MainLogger

logger: Logger = MainLogger().get_logger()


class Property:
    def __init__(self, file_path: str):
        path_utils.check_file_exists(file_path)
        self.__file_name = file_path

    def get_property_mandatory(self, key: str) -> str:
        key_array = key.split('.')
        if len(key_array) < 1:
            raise ValueError(f'Incorrect key value: {key}')
        with open(self.__file_name, 'r') as file:
            props = yaml.safe_load(file)
            current_properties_tree = props
            for current_key in key_array:
                current_properties_tree = current_properties_tree[current_key]
        logger.info(f'Got property. Key: {key} Value: {current_properties_tree}')
        return current_properties_tree

    def get_property(self, key: str, default: str) -> str:
        try:
            return self.get_property_mandatory(key)
        except KeyError:
            logger.warning(f'Cannot get property: {key}. Default value will be used')
            return default
        except TypeError:
            logger.warning(f'Cannot get property: {key}. Default value will be used')
            return default
