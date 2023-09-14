with open("input.txt", "r") as file:
    txt = file.read().strip()
    

# txt = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

i = 0
message_length = 14

while i < len(txt) - 1:
    if len(set(txt[i:i + message_length:])) == message_length:
        break
    i += 1

print(i + message_length)