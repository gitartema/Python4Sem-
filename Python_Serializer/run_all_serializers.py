from Serializer.serializer_creator import SerializerCreator
import argparse
from test import arguments_for_test


object_to_serialize = arguments_for_test.Objects()

def serialize(python_object, file_to_serialize):
    serializer = SerializerCreator.create_serializer(file_to_serialize)

    serializer.dump(python_object, file_to_serialize)
    serialize_str = serializer.dumps(python_object)

    deserialize_object = serializer.load(file_to_serialize)
    deserialize_object_from_str = serializer.loads(serialize_str)

    #print(serialize_str)

    #print(deserialize_object_from_str)
    
    #function result
    print(deserialize_object_from_str(1, 2, 3))

    #print(deserialize_object)
    
    #function result
    print(deserialize_object(1, 2, 3))



def main():
    serialize(object_to_serialize.lambda_function, "test.json")
    serialize(object_to_serialize.lambda_function, "test.yaml")
    serialize(object_to_serialize.lambda_function, "test.toml")
    serialize(object_to_serialize.lambda_function, "test.pickle")
    
    print('Completed!')


if __name__ == "__main__":
    main()
