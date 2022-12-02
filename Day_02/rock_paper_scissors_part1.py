# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
# Opponents: A for Rock, B for Paper, and C for Scissors
# Me: X for Rock, Y for Paper, and Z for Scissors
# Score_Allocation : 1 for Rock, 2 for Paper, and 3 for Scissors
# Overall_Score
score_data = open("input.txt").read()
score = 0
for i in score_data.split("\n"):
    opponent, me = i.split()

    if me == "X":
        if opponent == "C":
            score += 6
        if opponent == "A":
            score += 3
        score += 1

    if me == "Y":
        if opponent == "A":
            score += 6
        if opponent == "B":
            score += 3
        score += 2

    if me =="Z":
        if opponent == "B":
            score += 6
        if opponent == "C":
            score += 3
        score += 3

print(score)