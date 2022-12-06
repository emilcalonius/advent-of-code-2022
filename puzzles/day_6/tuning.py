# PART 1. & PART 2.
def find_start(string, number):
    char_set = set()
    for i in range(len(string)):
        for j in range(number):
            char_set.add(string[i+j])
        if len(char_set) == number:
            return i+number
        char_set.clear()
    return 0


with open("datastream.txt", "r") as file:
    print(find_start(file.readline(), 4))

with open("datastream.txt", "r") as file:
    print(find_start(file.readline(), 14))