with open("input.txt", "r") as file:
    txt = file.read().split("\n")

# A = rock
# B = paper
# C = scissor

# rock - 1 point
# paper - 2 points
# scissors - 3 points

# X - 0 for loss
# Y - 3 for tie
# Z - 6 for win

strategy = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6
    }

score = 0

for move in txt:
    score += strategy[move]

print(score)