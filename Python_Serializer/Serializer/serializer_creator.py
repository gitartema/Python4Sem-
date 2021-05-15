from Serializer import json_serializer
from Serializer import yaml_serializer
from Serializer import toml_serializer
from Serializer import pickle_serializer

class SerializerCreator():

    @classmethod
    def create_serializer(cls, file_to_serialize):
        try:
            file_format = file_to_serialize.split(".")[1]
        except:
            raise Exception("Incorrect format")

        if file_format == 'json':
            return json_serializer.JsonSerializer()
        elif file_format == 'yaml':
            return yaml_serializer.YamlSerializer()
        elif file_format == 'toml':
            return toml_serializer.TomlSerializer()
        elif file_format == 'pickle':
            return pickle_serializer.PickleSerializer()
        else:
            raise Exception("Incorrect format")