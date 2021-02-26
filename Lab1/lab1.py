FILENAME = "file.txt"

strings = list()
 
for i in range(3):
    string = input("Enter " + str(i+1) + " string: ")
    strings.append(string + "\n")

with open(FILENAME, "a") as file:
    for string in strings:
        file.write(string)
 
print("File data:")
with open(FILENAME, "r") as file:
    for string in file:
        print(string, end="")