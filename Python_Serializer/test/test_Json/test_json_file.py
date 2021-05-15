import unittest
import sys

sys.path.append('../')
import arguments_for_test

sys.path.append('../../')
from Serializer.json_serializer import JsonSerializer

serializer = JsonSerializer()
test_object = arguments_for_test.Objects()

class TestJsonFileSerializer(unittest.TestCase):

    def test_int_serialization_to_file(self):
        object_to_serialize = test_object.integer
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_string_serialization_to_file(self):
        object_to_serialize = test_object.string
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_float_serialization_to_file(self):
        object_to_serialize = test_object.floating
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_tuple_serialization_to_file(self):
        object_to_serialize = test_object.tuple
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_list_serialization_to_file(self):
        object_to_serialize = test_object.list
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_dict_serialization_to_file(self):
        object_to_serialize = test_object.dict
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_simple_function_serialization_to_file(self):
        object_to_serialize = test_object.simple_function
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize(), object_after_deserialize())


    def test_recursive_function_serialization_to_file(self):
        object_to_serialize = test_object.recursive_function
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize(2), object_after_deserialize(2))


    def test_global_function_serialization_to_file(self):
        object_to_serialize = test_object.global_function
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize(2), object_after_deserialize(2))


    def test_lambda_function_serialization_to_file(self):
        object_to_serialize = test_object.lambda_function
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize(1, 2, 3), object_after_deserialize(1, 2, 3))


    def test_simple_class_serialization_to_file(self):
        object_to_serialize = arguments_for_test.SimpleClass
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_not_simple_class_serialization_to_file(self):
        object_to_serialize = arguments_for_test.NotSimpleClass
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize, object_after_deserialize)


    def test_class_object_serialization_to_file(self):
        object_to_serialize = arguments_for_test.SimpleClass('Artem', 19)
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize.name, object_after_deserialize.name)


    def test_function_in_class_serialization_to_file(self):
        object_to_serialize = arguments_for_test.NotSimpleClass(10, 3, test_object)
        serializer.dump(object_to_serialize, 'test.json')
        object_after_deserialize = serializer.load('test.json')
        self.assertEqual(object_to_serialize.sum_with_exponentation(12), 
            object_after_deserialize.sum_with_exponentation(12))



if __name__ == '__main__':
    unittest.main()