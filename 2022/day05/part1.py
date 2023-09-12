with open("input.txt", "r") as file:
    txt = file.read().strip().split("\n")

stacks = {
    1: ["J", "H", "P", "M", "S", "F", "N", "V"],
    2: ["S", "R", "L", "M", "J", "D", "Q"],
    3: ["N", "Q", "D", "H", "C", "S", "W", "B"],
    4: ["R", "S", "C", "L"],
    5: ["M", "V", "T", "P", "F", "B"],
    6: ["T", "R", "Q", "N", "C"],
    7: ["G", "V", "R"],
    8: ["C", "Z", "S", "P", "D", "L", "R"],
    9: ["D", "S", "J", "V", "G", "P", "B", "F"]
}


# [V]     [B]                     [F]
# [N] [Q] [W]                 [R] [B]
# [F] [D] [S]     [B]         [L] [P]
# [S] [J] [C]     [F] [C]     [D] [G]
# [M] [M] [H] [L] [P] [N]     [P] [V]
# [P] [L] [D] [C] [T] [Q] [R] [S] [J]
# [H] [R] [Q] [S] [V] [R] [V] [Z] [S]
# [J] [S] [N] [R] [M] [T] [G] [C] [D]
#  1   2   3   4   5   6   7   8   9 



for move in txt:
    print(move)
    amount_to_move = int(move.split(" ")[1])
    from_stack = int(move.split(" ")[3])
    to_stack = int(move.split(" ")[5])

    items_being_moved = stacks[from_stack][-amount_to_move::]
    del stacks[from_stack][-amount_to_move::]
    stacks[to_stack].extend(items_being_moved[::-1])
    print(stacks)

message = ""

for stack in stacks.values():
    message += stack[-1]

print(message)

stacks = {
    1: ["Z", "N"],
    2: ["M", "C", "D"],
    3: ["P"]
}

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 



