import math

with open("input.txt", "r") as file:
    lines = file.readlines()


visited = {(0, 0)}
# 0, 0 origin is top left
move = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}

hx, hy, tx, ty = 0, 0, 0, 0

for instruction in lines:
    direction, distance = instruction.split(" ")
    m = move[direction]
    for _ in range(int(distance)):
        # move head
        hx, hy = hx + m[0], hy + m[1]

        # update tail
        dx, dy = hx - tx, hy - ty
        if abs(dx) > 1 or abs(dy) > 1:
            if dx:
                tx += math.copysign(1, dx)
            if dy:
                ty += math.copysign(1, dy)
            visited.add((tx, ty))

print(len(visited))