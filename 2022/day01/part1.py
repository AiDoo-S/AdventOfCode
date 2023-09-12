with open("input.txt", "r") as file:
    txt = file.read().split("\n\n")
    
highest = 0

for elf in txt:
    elf = elf.split("\n")
    sum = 0
    for calorie_count in elf:
        sum += int(calorie_count)

    if sum > highest:
        highest = sum

print(highest)