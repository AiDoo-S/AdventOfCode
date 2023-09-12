with open("input.txt", "r") as file:
    txt = file.read().strip().split("\n")

amount_contained = 0

for pair in txt:
    first_pair = pair.split(",")[0]
    second_pair = pair.split(",")[1]

    first = int(first_pair.split("-")[0])
    second = int(first_pair.split("-")[1])
    third = int(second_pair.split("-")[0])
    fourth = int(second_pair.split("-")[1])
    if first == third and second == fourth:
        amount_contained += 1
    elif first <= third and second >= fourth:
        amount_contained += 1
    elif third <= first and fourth >= second:
        amount_contained += 1


print(amount_contained)
        