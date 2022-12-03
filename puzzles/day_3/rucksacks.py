import math
import re

# PART 1.
sum = 0
with open("rucksacks.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")

        # Separate line into two equally long strings
        compartment_1 = line[:int(math.floor(len(line)) / 2)]
        compartment_2 = line[int(math.floor(len(line)) / 2):]

        # Remove duplicate letters from new strings
        compartment_1 = "".join(set(compartment_1))
        compartment_2 = "".join(set(compartment_2))

        for char in compartment_1:
            if char in compartment_1 and char in compartment_2:
                if bool(re.search("[a-z]", char)):
                    sum += ord(char) - ord("a") + 1
                elif bool(re.search("[A-Z]", char)):
                    sum += ord(char) - ord("A") + 27
print(sum)

# PART 1.
sum = 0
group = []
with open("rucksacks.txt", "r") as file:
    for line in file:
        group.append("".join(set(line.rstrip("\n"))))

        if len(group) == 3:
            for char in group[1]:
                if char in group[0] and char in group[1] and char in group[2]:
                    if bool(re.search("[a-z]", char)):
                        sum += ord(char) - ord("a") + 1
                    elif bool(re.search("[A-Z]", char)):
                        sum += ord(char) - ord("A") + 27
            group.clear()
print(sum)
