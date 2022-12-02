# PART 1.
score = 0
with open("results.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        moves = line.split(" ")
        if moves[1] == "X":
            score += 1
            # Draw
            if moves[0] == "A":
                score += 3
            # Win
            elif moves[0] == "C":
                score += 6

        if moves[1] == "Y":
            score += 2
            # Draw
            if moves[0] == "B":
                score += 3
            # Win
            elif moves[0] == "A":
                score += 6

        if moves[1] == "Z":
            score += 3
            # Draw
            if moves[0] == "C":
                score += 3
            # Win
            elif moves[0] == "B":
                score += 6

print("Final score: " + str(score))

# PART 2.
score = 0
with open("results.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        moves = line.split(" ")
        if moves[1] == "Z":
            score += 6
            # Play paper
            if moves[0] == "A":
                score += 2
            # Play rock
            elif moves[0] == "C":
                score += 1
            # Play scissors
            else:
                score += 3

        if moves[1] == "Y":
            score += 3
            # Play paper 
            if moves[0] == "B":
                score += 2
            # Play rock
            elif moves[0] == "A":
                score += 1
            # Play scissors
            else:
                score += 3

        if moves[1] == "X":
            # Play paper
            if moves[0] == "C":
                score += 2
            # Play rock
            elif moves[0] == "B":
                score += 1
            # Play scissors
            else:
                score += 3

print("Final score: " + str(score))