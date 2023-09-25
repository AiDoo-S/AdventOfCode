with open("input.txt", "r") as file:
    grid = [list(map(int, line.strip())) for line in file.readlines()]

def check_visibility(grid, r, c):
    if c == 0 or c == C-1 or r == 0 or r == R -1:
        return 1
    # look left
    if all(grid[r][cc] < grid[r][c] for cc in range(c)):
        return 1
    # look right
    if all(grid[r][cc] < grid[r][c] for cc in range(c + 1, C)):
        return 1
    # look up
    if all(grid[rr][c] < grid[r][c] for rr in range(r)):
        return 1
    # look down
    if all(grid[rr][c] < grid[r][c] for rr in range(r + 1, R)):
        return 1
    
    return 0

count = 0

R = len(grid)
C = len(grid[0])

for r in range(R):
    for c in range(C):
        count += check_visibility(grid, r, c)

print(count)
