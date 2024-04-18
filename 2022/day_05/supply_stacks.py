import copy

#----------------------------------- PART 1. -----------------------------------------
# Firs read the containers from the input file and create stacks in code
original_stacks = []
with open("crates.txt", "r") as file:
    # Find the number of stacks in the file
    first_line = file.readline()
    n_of_stacks = int((len(first_line) - 8) / 3)
    # Create n lists
    original_stacks = [[] for _ in range(n_of_stacks)]
    # Move to the first line in the file and start reading containers
    file.seek(0)
    lines = file.readlines()
    # Remove last line because it does not contain any containers
    lines.pop()
    lines.reverse()
    for line in lines:
        new_line = ""
        line = line.strip("\n")
        for i in range(len(line)):
            # Replace every 4th character
            if (i + 1) % 4 == 0:
                new_line += "-"
            else:
                new_line += line[i]
        line = new_line
        line = line.replace("[", "").replace("]", "").replace("   ", "_")
        containers = line.split("-")
        
        i = 0
        for container in containers:
            if container != "_":
                original_stacks[i].append(container)
            i += 1

stacks = copy.deepcopy(original_stacks)

print("Stacks at the beginning of part 1:")
for stack in stacks:
    print(stack)
print()

# Do the given operations on the stacks
with open("steps.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        command = line.split(" ")
        amount = int(command[1])
        from_stack = int(command[3])-1
        to_stack = int(command[5])-1
        for n in range(amount):
            stacks[to_stack].append(stacks[from_stack].pop())

solution = ""
print("Stacks at the end with method 1:")
for stack in stacks:
    print(stack)
    solution += stack[len(stack)-1]
print()
print("Solution string is: " + solution)
print()

#------------------------------------ PART 2. -------------------------------------------
# Get the original arrangement of the stacks
stacks = copy.deepcopy(original_stacks)

print("Stacks at the beginning of part 2:")
for stack in stacks:
    print(stack)
print()

# Do the given operations on the stacks
with open("steps.txt", "r") as file:
    temp_stack = []
    for line in file:
        line = line.rstrip("\n")
        command = line.split(" ")
        amount = int(command[1])
        from_stack = int(command[3])-1
        to_stack = int(command[5])-1
        # Move containers first to a temporary stack
        for n in range(amount):
            temp_stack.append(stacks[from_stack].pop())
        # And then into the correct stack
        for n in range(amount):
            stacks[to_stack].append(temp_stack.pop())

solution = ""
print("Stacks at the end with method 2:")
for stack in stacks:
    print(stack)
    solution += stack[len(stack)-1]
print()
print("Solution string is: " + solution)
print()