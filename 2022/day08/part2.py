with open("input.txt", "r") as file:
    grid = [list(map(int, line.strip())) for line in file.readlines()]

def check_scenic_score(grid, r, c):
    if c == 0 or c == C-1 or r == 0 or r == R -1:
        return 0
    
    for dc in range(1, c + 1):
        if grid[r][c - dc] >= grid[r][c]:
            break
    left = dc

    for dc in range(1, C - c):
        if grid[r][c + dc] >= grid[r][c]:
            break
    right = dc

    for dr in range(1, r + 1):
        if grid[r - dr][c] >= grid[r][c]:
            break
    top = dr

    for dr in range(1, R - r):
        if grid[r + dr][c] >= grid[r][c]:
            break
    bottom = dr
    return left * right * top * bottom

score = 0

R = len(grid)
C = len(grid[0])

for r in range(R):
    for c in range(C):
        score = max(score, check_scenic_score(grid, r, c))

print(score)
