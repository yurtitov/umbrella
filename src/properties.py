import yaml


class Property:
    def __init__(self, file_name: str):
        self.__file_name = file_name

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
