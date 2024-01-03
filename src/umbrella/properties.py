import yaml
import os.path


class Property:
    def __init__(self, file_path: str):
        self.__check_file_exists(file_path)
        self.__file_name = file_path

    def get_property_mandatory(self, key: str) -> str:
        key_array = key.split('.')
        if len(key_array) < 1:
            raise ValueError(f'Incorrect key value: {key}')
        with open(self.__file_name, 'r') as file:
            props = yaml.safe_load(file)
            sdf = props
            for k in key_array:
                sdf = sdf[k]
        return sdf

    def get_property(self, key: str, default: str) -> str:
        try:
            return self.get_property_mandatory(key)
        except KeyError:
            return default
        except TypeError:
            return default

    @staticmethod
    def __check_file_exists(file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f'File not found: {file_path}')
