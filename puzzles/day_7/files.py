# --------------------------------------- PART 1. & PART 2. -------------------------------------------
with open("commands.txt", "r") as file:
    dirs = dict()
    current_dir = []
    for line in file:
        line = line.rstrip("\n")
        commands = line.split(" ")
        if commands[0] == "$":
            if commands[1] == "cd":
                if commands[2] == "..":
                    current_dir.pop()
                elif commands[2] == "/":
                    current_dir.append("/")
                    while len(current_dir) > 1:
                        current_dir.pop()
                else:
                    if len(current_dir) > 1:
                        current_dir.append(current_dir[len(current_dir)-1] + "/" + commands[2])
                    elif len(current_dir) == 1:
                        current_dir.append(current_dir[len(current_dir)-1] + commands[2])
                    else:
                        current_dir.append(commands[2])
        elif commands[0] != "dir":
            for dir in current_dir:
                if dir in dirs:
                    dirs[dir] += int(commands[0])
                else:
                    dirs[dir] = int(commands[0])

# Sum of all the folders with size less than or equal to 100 000
print("Sum of folders smaller than 100 000 by size:")
print(sum(list(filter(lambda x: x <= 100000, dirs.values()))))

max_space = 70000000
required_space = 30000000
free_space = max_space - dirs["/"]

print("Smallest possible folder by size to delete to run update:")
print(min(list(filter(lambda x: x >= required_space-free_space, dirs.values()))))