with open("input.txt", "r") as file:
    txt = file.read().strip()
    

# txt = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

i = 0

while i < len(txt) - 1:
    if len(set(txt[i:i + 4:])) == 4:
        break
    i += 1

print(i + 4)