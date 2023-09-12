with open("input.txt", "r") as file:
    txt = file.read().split("\n\n")

calorie_sums = []

for elf in txt:
    elf = elf.split("\n")
    calorie_sum = 0
    for calorie_count in elf:
        calorie_sum += int(calorie_count)
    
    calorie_sums.append(calorie_sum)
        
print(sum(sorted(calorie_sums)[-3:]))