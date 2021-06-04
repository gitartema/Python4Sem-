import os
import sys

sys.path.append('../../')

import Python_Serializer


def func(cls, a, b):
    return a + b


def class_creator(path):
    class_attrs_to_file = {'name': 'Person', 'age': 18, 'func': func}

    serializer = Python_Serializer.JsonSerializer()

    serializer.dump(class_attrs_to_file, path)

    class_attrs_from_file = serializer.load(path)
    return type('NewClass', (), class_attrs_from_file)


def main():
    # /home/artem/Python/Python4Sem/tasks/Metaclass_from_file/file.json
    path = input("Enter path to file: ").strip()

    if os.path.exists(path) and path.split(".")[-1] == 'json':
        NewClass = class_creator(path)
        print(NewClass.name)

        new_class_obj = NewClass()
        print(new_class_obj.func(1, 2))

        new_class_obj_2 = class_creator(path)()
        print(new_class_obj_2.func(3, 4))
    else:
        raise Exception('Incorrect input!')


if __name__ == '__main__':
    main()
