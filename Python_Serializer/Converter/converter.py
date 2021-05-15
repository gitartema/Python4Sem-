import json
import pickle
import toml
import yaml

class Converter():
    def __init__(self, input_file, new_file_format):
        self.input_file = input_file
        self.new_file_format = new_file_format
        self.file_format = input_file.split(".")[1]
        self.file_after_convert = input_file.split(".")[0] + '.' + new_file_format
        self.data = None

        self.read_file = {
            'json': self.read_from_json,
            'yaml': self.read_from_yaml,
            'toml': self.read_from_toml,
            'pickle': self.read_from_pickle
        }
        self.write_file = {
            'json': self.write_to_json,
            'yaml': self.write_to_yaml,
            'toml': self.write_to_toml,
            'pickle': self.write_to_pickle
        }


    def read_from_json(self):
        with open(self.input_file, 'r') as rf:
            return json.load(rf)

    def read_from_yaml(self):
        with open(self.input_file, 'r') as rf:
            return yaml.load(rf, Loader=yaml.Loader)

    def read_from_toml(self):
        with open(self.input_file, 'r') as rf:
            return toml.load(rf)        

    def read_from_pickle(self):
        with open(self.input_file, 'rb') as rfb:
            return pickle.load(rfb)

    def write_to_json(self):
        with open(self.file_after_convert, 'w+') as wf:
            json.dump(self.data, wf, indent=4)
    
    def write_to_yaml(self):
        with open(self.file_after_convert, 'w+') as wf:
            yaml.dump(self.data, wf)

    def write_to_toml(self):
        with open(self.file_after_convert, 'w+') as wf:
            toml.dump(self.data, wf)

    def write_to_pickle(self):
        with open(self.file_after_convert, 'w+b') as wfb:
            pickle.dump(self.data, wfb)
    


    def convert(self):
        if self.file_format == self.new_file_format:
            return 'Yoy entered the same formats'

        try:
            self.data = self.read_file[self.file_format]()
            self.write_file[self.new_file_format]()
            return 'Completed!'
        except FileNotFoundError:
            return 'File not found!'
        except KeyError:
            return 'Wrong file extension!'