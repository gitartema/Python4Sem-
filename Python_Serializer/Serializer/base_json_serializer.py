import json
from Serializer.serializer import Serializer

class BaseJsonSerializer(Serializer):
    @classmethod
    def is_seriazable(cls, python_object):
         try:
            json.dumps(python_object)
            return True
         except TypeError:
            return False

    @classmethod
    def get_json_str(cls, python_object):
        obj_type = cls.get_object_type(python_object)

        is_default_serializible = cls.is_seriazable(python_object)
 
        json_str = {
            'object': repr(python_object),
            'type': obj_type,
            'serializable_by_default': is_default_serializible,
            'name': cls.get_object_name(python_object),
            'value': python_object if is_default_serializible
                            else None,
            'dict_class': cls.class_to_dict(python_object),
            'args': cls.get_function_arguments(python_object),
            'code': cls.get_source_code(python_object),
            'base64': cls.get_base64_pickle_object(python_object)
        }

        return json_str

    @classmethod
    def deserialize_data(cls, json_object):
        return cls.get_object_from_base64(json_object.get('base64'))

    @classmethod
    def write_to_json(cls, python_object, file_name):
        with open(file_name, 'w') as wf:
            json.dump(python_object, wf, indent=4)

    @classmethod
    def read_from_json(cls, file_name):
        with open(file_name, 'r') as rf:
            return json.load(rf)