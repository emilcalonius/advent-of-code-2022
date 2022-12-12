with open("moves.txt") as file:
    head = [0, 0]
    tail = [0, 0]
    visited = set()
    visited.add(tuple(tail))
    for line in file:
        line = line.rstrip("\n")
        commands = line.split(" ")
        direction = commands[0]
        amount = int(commands[1])

        for i in range(amount):
            if direction == "U":
                head[1] += 1
            if direction == "D":
                head[1] -= 1
            if direction == "R":
                head[0] += 1
            if direction == "L":
                head[0] -= 1

            if abs(head[0] - tail[0]) + abs(head[1] - tail[1]) == 3:
                if head[0] - tail[0] == 1:
                    tail[0] += 1
                if head[0] - tail[0] == -1:
                    tail[0] -= 1
                if head[1] - tail[1] == 1:
                    tail[1] += 1
                if head[1] - tail[1] == -1:
                    tail[1] -= 1

            if head[0] - tail[0] == 2:
                tail[0] += 1
            if head[0] - tail[0] == -2:
                tail[0] -= 1
            if head[1] - tail[1] == 2:
                tail[1] += 1
            if head[1] - tail[1] == -2:
                tail[1] -= 1
            
            visited.add(tuple(tail))

    print(len(visited))