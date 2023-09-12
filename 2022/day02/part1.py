with open("input.txt", "r") as file:
    txt = file.read().split("\n")

# A = rock
# B = paper
# C = scissor

# X = rock - 1 point
# Y = paper - 2 points
# Z = scissors - 3 points

# 0 for loss
# 3 for tie
# 6 for win

strategy = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3
    }

score = 0

for move in txt:
    score += strategy[move]

print(score)