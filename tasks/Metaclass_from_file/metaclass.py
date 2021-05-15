import ast

dict_from_file = {}

with open("file.txt", 'r') as rf:
    for line in rf:
        #text = rf.read()
        key = line.split(" ")[0]
        value = line.split(" ")[1:]
        dict_from_file[key] = value.rstrip()

#dict_from_file = ast.literal_eval(text)
print(dict_from_file)

NewClass = type('NewClass', (), {})