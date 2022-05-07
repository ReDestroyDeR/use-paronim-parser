with open("paronims.txt") as file:
    data = file.readlines()


dictionary_set = set(line.lower() for line in data)
while 1:
    _word = input("Search query: ")
    _found = []
    for line in dictionary_set:
        if line.find(_word.lower()) != -1:
            line = line.replace(_word.lower(), _word.upper())
            _found.append(line.strip())
            

    if len(_found) == 0:
        print("Nothing found")
        continue

    for line in _found:
        print(line)
