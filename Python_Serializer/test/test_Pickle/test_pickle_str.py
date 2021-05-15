import unittest
import sys

sys.path.append('../')
import arguments_for_test

sys.path.append('../../')
from Serializer.pickle_serializer import PickleSerializer

serializer = PickleSerializer()
test_object = arguments_for_test.Objects()

class TestJsonStrSerializer(unittest.TestCase):

    def test_int_serialization_to_file(self):
        object_to_serialize = test_object.integer
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_string_serialization_to_file(self):
        object_to_serialize = test_object.string
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_float_serialization_to_file(self):
        object_to_serialize = test_object.floating
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_tuple_serialization_to_file(self):
        object_to_serialize = test_object.tuple
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_list_serialization_to_file(self):
        object_to_serialize = test_object.list
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_dict_serialization_to_file(self):
        object_to_serialize = test_object.dict
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_simple_function_serialization_to_file(self):
        object_to_serialize = test_object.simple_function
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize(), object_after_deserialize())


    def test_recursive_function_serialization_to_file(self):
        object_to_serialize = test_object.recursive_function
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize(2), object_after_deserialize(2))


    def test_global_function_serialization_to_file(self):
        object_to_serialize = test_object.global_function
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize(2), object_after_deserialize(2))


    def test_lambda_function_serialization_to_file(self):
        object_to_serialize = test_object.lambda_function
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize(1, 2, 3), object_after_deserialize(1, 2, 3))


    def test_simple_class_serialization_to_file(self):
        object_to_serialize = arguments_for_test.SimpleClass
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_not_simple_class_serialization_to_file(self):
        object_to_serialize = arguments_for_test.NotSimpleClass
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_class_object_serialization_to_file(self):
        object_to_serialize = arguments_for_test.SimpleClass('Artem', 19)
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize.name, object_after_deserialize.name)


    def test_function_in_class_serialization_to_file(self):
        object_to_serialize = arguments_for_test.NotSimpleClass(10, 3, test_object)
        str_after_serialize = serializer.dumps(object_to_serialize)
        object_after_deserialize = serializer.loads(str_after_serialize)
        self.assertEqual(object_to_serialize.sum_with_exponentation(12), 
            object_after_deserialize.sum_with_exponentation(12))


if __name__ == '__main__':
    unittest.main()