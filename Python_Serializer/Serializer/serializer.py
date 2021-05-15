import inspect
import pickle
import cloudpickle
import base64
from Serializer.serialize_methods import SerializeMethods


class Serializer(SerializeMethods):

    @classmethod
    def get_object_type(cls, python_object):
        if inspect.isclass(python_object):
            return 'class'
        else:
            return str(type(python_object)).split('\'')[1]

    @classmethod
    def get_object_name(cls, python_object):
        try:
            return python_object.__name__
        except AttributeError:
            return None

    @classmethod
    def class_to_dict(cls, class_to_serialize):
        try:
            return {key: str(value) for key, value in class_to_serialize.__dict__.items()}
        except AttributeError:
            return {}

    @classmethod
    def get_function_arguments(cls, function_to_serialize):
        list_type_args = [
            'args', 'varargs', 'varkw', 'defaults',
            'kwonlyargs', 'kwonlydefaults', 'annotations',
        ]
        try:
            return {
                arg_name: args for (arg_name, args) in
                zip(list_type_args, inspect.getfullargspec(function_to_serialize))
            }
        except TypeError:
            return {}

    @classmethod
    def get_source_code(cls, python_object):
        try:
            return inspect.getsource(python_object).split('\n')
        except TypeError:
            return []

    @classmethod
    def get_base64_pickle_object(cls, python_object):
        try:
            if cls.is_lambda_function(python_object):
                pickle_str = cloudpickle.dumps(python_object)
                return base64.b64encode(pickle_str).decode('ascii')

            return base64.b64encode(pickle.dumps(python_object)).decode('ascii')
        except TypeError:
            return None

    @classmethod
    def get_object_from_base64(cls, base64_object):
        try:
            return pickle.loads(base64.b64decode(base64_object.encode('ascii')))
        except AttributeError:
            return None

    @classmethod
    def is_lambda_function(cls, python_object):
        try:
            elements = python_object.__name__.split('<')
        except AttributeError:
            return False

        if len(elements) > 1:
            function_name = elements[1]
            elements = function_name.split('>')
            function_name = elements[0]

            if function_name == "lambda":
                return True
            else:
                return False
        else:
            return False
