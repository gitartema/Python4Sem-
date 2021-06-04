import pickle
import cloudpickle
from Serializer.base_json_serializer import BaseJsonSerializer


class PickleSerializer(BaseJsonSerializer):
    @classmethod
    def dump(cls, python_object, file_name):
        try:
            with open(file_name, 'wb') as wfb:
                if(cls.is_lambda_function(python_object)):
                    pickle.dump(cloudpickle.dumps(python_object), wfb)
                else:
                    pickle.dump(python_object, wfb)
        except TypeError:
            pass

    @classmethod
    def dumps(cls, python_object):
        try:
            if(cls.is_lambda_function(python_object)):
                return cloudpickle.dumps(python_object)
            else:
                return pickle.dumps(python_object)
        except TypeError:
            return None

    @classmethod
    def load(cls, file_name):
        try:
            with open(file_name, 'rb') as rfb:
                object_from_file = pickle.load(rfb)
            with open(file_name, 'rb') as rfb:
                if type(object_from_file) is bytes:
                    return pickle.loads(pickle.load(rfb))
                else:
                    return pickle.load(rfb)
        except (FileNotFoundError, TypeError):
            return None

    @classmethod
    def loads(cls, str_to_deserialize):

        try:
            return pickle.loads(str_to_deserialize)
        except TypeError:
            return None
