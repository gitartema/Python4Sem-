import json
from Serializer.base_json_serializer import BaseJsonSerializer

class JsonSerializer(BaseJsonSerializer):
    @classmethod
    def dump(cls, python_object, file_name):
        try:
            BaseJsonSerializer.write_to_json(BaseJsonSerializer.get_json_str(python_object), file_name)
        except (TypeError, OSError):
            raise OSError

    @classmethod    
    def dumps(cls, python_object):
        try:
            return json.dumps(BaseJsonSerializer.get_json_str(python_object), indent=4)
        except TypeError:
            return None

    @classmethod
    def load(cls, file_name):
        try:
            return BaseJsonSerializer.deserialize_data(BaseJsonSerializer.read_from_json(file_name))
        except TypeError:
            return None

    @classmethod
    def loads(cls, str_to_deserialize):
        try:
            return BaseJsonSerializer.deserialize_data(json.loads(str_to_deserialize))
        except TypeError:
            return None