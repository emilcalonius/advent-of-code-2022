with open("moves.txt") as file:
    knots = [[0, 0] for _ in range(10)]
    tail = [0, 0]
    visited = set()
    visited.add(tuple(tail))
    for line in file:
        line = line.rstrip("\n")
        commands = line.split(" ")
        direction = commands[0]
        amount = int(commands[1])

        for i in range(amount):
            for j in range(1, 10):
                current = knots[j - 1]
                prev = knots[j]

                if j == 1:
                    if direction == "U":
                        current[1] += 1
                    if direction == "D":
                        current[1] -= 1
                    if direction == "R":
                        current[0] += 1
                    if direction == "L":
                        current[0] -= 1

                if abs(current[0] - prev[0]) + abs(current[1] - prev[1]) == 3:
                    if current[0] - prev[0] == 1:
                        prev[0] += 1
                    if current[0] - prev[0] == -1:
                        prev[0] -= 1
                    if current[1] - prev[1] == 1:
                        prev[1] += 1
                    if current[1] - prev[1] == -1:
                        prev[1] -= 1

                if current[0] - prev[0] == 2:
                    prev[0] += 1
                if current[0] - prev[0] == -2:
                    prev[0] -= 1
                if current[1] - prev[1] == 2:
                    prev[1] += 1
                if current[1] - prev[1] == -2:
                    prev[1] -= 1
                
                if(j == 9):
                    visited.add(tuple(prev))

    print(len(visited))