x = 1
cycle = 1
values = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        commands = line.split(" ")

        if commands[0] == "addx":
            for i in range(2):
                if cycle in [20, 60, 100, 140, 180, 220]:
                    values.append(cycle * x)
                cycle += 1
            x += int(commands[1])
        else:
            if cycle in [20, 60, 100, 140, 180, 220]:
                values.append(cycle * x)
            cycle += 1

print(sum(values))