calories_arr = []
calories = 0

with open("calories.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line == "":
            calories_arr.append(calories)
            calories = 0
            continue
        calories += int(line)

max_calories = max(calories_arr)
print("Most calories carried: " + str(max_calories) + 
" calories by elf #" + str(calories_arr.index(max_calories) + 1))

temp_arr = calories_arr.copy()
# Change n_of_elves according to how many of the elves with most calories you want to find
n_of_elves = 3
max_n_calories = []

for n in range(0, n_of_elves, 1):
    max_calories = max(temp_arr)
    max_n_calories.append(max_calories)
    temp_arr.remove(max_calories)

print()
print("Top "+ str(n_of_elves) + " elves:")
i = 1

for c in max_n_calories:
    print(str(i) + ". Elf #" + str(calories_arr.index(c) + 1) + " with " + str(c) + " calories")
    i += 1

print()
print("Total calories for top 3 elves: " + str(sum(max_n_calories)))