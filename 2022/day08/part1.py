from copy import deepcopy

with open("input.txt", "r") as file:
    txt = file.read().strip().split("\n")

txt = """30373
25512
65332
33549
35390""".split("\n")


def check_visibility(value, i, j):
    # up
    if all(x >= value for x in txt[0:i][j]):
        print("bad")
    # right
    # down
    # left

    return True

count = 0

# Count edges
count += len(txt) * 2 + (len(txt[0]) - 2) * 2

# Count visible

i = 1
j = 1
print(txt)
while i < len(txt[0]) - 1:
    top_visible = False
    right_visible = False
    bottom_visible = False
    left_visible = False
    j = 1
    while j < len(txt) - 1:
        # print(f"i: {i}")
        # print(f"j: {j}")
        # print(txt[i][j])
        if check_visibility(txt[i][j], i, j):
            count += 1
        j += 1

    i += 1

print(count)
