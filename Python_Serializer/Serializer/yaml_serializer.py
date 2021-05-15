import yaml
from Serializer.base_json_serializer import BaseJsonSerializer

class YamlSerializer(BaseJsonSerializer):
    @classmethod
    def dump(cls, python_object, file_name):
        try:
            json_template = BaseJsonSerializer.get_json_str(python_object)
            with open(file_name, 'w') as wf:
                return yaml.dump(json_template, wf)
        except TypeError:
            pass
        
    @classmethod    
    def dumps(cls, python_object):
        try:
            json_template = BaseJsonSerializer.get_json_str(python_object)
            return yaml.dump(json_template)
        except TypeError:
            return None

    @classmethod
    def load(cls, file_name):
        try:
            with open(file_name, 'r') as rf:
                obj = yaml.load(rf, Loader=yaml.Loader)
            return BaseJsonSerializer.deserialize_data(obj)
        except FileNotFoundError:
            return None
        except TypeError:
            return None

    @classmethod
    def loads(cls, str_to_deserialize):
        try:
            return BaseJsonSerializer.deserialize_data(yaml.load(str_to_deserialize, Loader=yaml.Loader))
        except AttributeError:
            return None