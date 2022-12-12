x = 1
cycle = 0
row = ""

with open("input.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        commands = line.split(" ")

        if commands[0] == "addx":
            for _ in range(2):
                if cycle % 40 in [x - 1, x, x + 1]:
                    print("#", end = "")
                else:
                    print(".", end = "")

                if cycle in [39, 79, 119, 159, 199, 239]:
                    print()

                cycle += 1
            x += int(commands[1])
        else:
            if cycle % 40 in [x - 1, x, x + 1]:
                print("#", end = "")
            else:
                print(".", end = "")

            if cycle in [39, 79, 119, 159, 199, 239]:
                print()
            
            cycle += 1