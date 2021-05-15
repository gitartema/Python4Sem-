global_value = 15


class Objects():
    def __init__(self):

        self.integer = 10

        self.string = 'Hello, World!'

        self.floating = 777.777

        self.tuple = ('qwwwqw', 12, True)

        self.list = [1, 2, 3, 'Hello, World']

        self.dict = {
            "squadName": "Super hero squad",
            "homeTown": "Metro City",
            "formed": 2016,
            "secretBase": "Super tower",
            "active": True,
            "members": [
                {
                        "name": "Molecule Man",
                        "age": 29,
                        "secretIdentity": "Dan Jukes",
                        "powers": [
                            "Radiation resistance",
                            "Turning tiny",
                            "Radiation blast"
                        ]
                },
                {
                    "name": "Madame Uppercut",
                    "age": 39,
                    "secretIdentity": "Jane Wilson",
                    "powers": [
                            "Million tonne punch",
                            "Damage resistance",
                            "Superhuman reflexes"
                    ]
                },
                {
                    "name": "Eternal Flame",
                    "age": 1000000,
                    "secretIdentity": "Unknown",
                    "powers": [
                            "Immortality",
                            "Heat Immunity",
                            "Inferno",
                            "Teleportation",
                            "Interdimensional travel"
                    ]
                }
            ]
        }

        self.tuple_for_toml = (1, 2, 3, 4, 5)

        self.list_for_toml = ['Hello', ',', 'World', '!']
        

    def simple_function(self):
        print('\nIt\'s print from function\n')
        return ('Hello, world!')

    def recursive_function(self, number):
        if number == 0:
            return True
        return self.recursive_function(number - 1)

    def global_function(self, a):
        return global_value**a

    lambda_function = lambda self, a, b, c: a + b + c


class SimpleClass():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.person_data = {'name+age': self.name +
                            str(self.age), 'have_18': self.have18()}

    def have18(self):
        if self.age >= 18:
            return True
        else:
            return False


class NotSimpleClass():
    def __init__(self, number, power, class_object):
        self.number = number
        self.power = power
        self.class_object = class_object
        self.list = [1, 2, 3, 'Hello, World']
        self.data = {
            'number': self.number,
            'power': self.power,
            'class': self.class_object,
            'exponentation': self.exponentation(),
            'list': self.list
        }
        

    def exponentation(self):
        return self.number ** self.power

    def sum_with_exponentation(self, a):
        return a + self.exponentation()
