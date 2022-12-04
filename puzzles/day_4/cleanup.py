#--------------------------------- PART 1. & PART 2. ----------------------------------
with open("assignments.txt", "r") as file:
    contains = 0
    overlaps = 0
    for line in file:
        line = line.rstrip("\n")
        areas = line.split(",")

        range1 = areas[0].split("-")
        range2 = areas[1].split("-")

        if(((int(range1[0]) >= int(range2[0]))
        and (int(range1[1])) <= int(range2[1]))
        or ((int(range2[0]) >= int(range1[0]))
        and (int(range2[1])) <= int(range1[1]))):
            contains += 1

        if((((int(range1[0]) >= int(range2[0])) and (int(range1[0]) <= int(range2[1])))
        or ((int(range1[1]) <= int(range2[1])) and (int(range1[1]) >= int(range2[0]))))
        or (((int(range2[0]) >= int(range1[0])) and (int(range2[0]) <= int(range1[1])))
        or ((int(range2[1]) <= int(range1[1])) and (int(range2[1]) >= int(range1[0]))))):
            overlaps += 1

print(contains)
print(overlaps)