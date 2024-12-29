# file = open("day 024/files/my_file.txt") #opening a file
# contents = file.read()
# print(contents)
# file.close()


with open("day 024/files/my_file.txt") as file: #opening a file
    contents = file.read()
    print(contents)
