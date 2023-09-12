with open("input.txt", "r") as file:
    txt = file.read().strip().split("\n")

values = {"a": 1,
          "b": 2,
          "c": 3,
          "d": 4,
          "e": 5,
          "f": 6,
          "g": 7,
          "h": 8,
          "i": 9,
          "j": 10,
          "k": 11,
          "l": 12,
          "m": 13,
          "n": 14,
          "o": 15,
          "p": 16,
          "q": 17,
          "r": 18,
          "s": 19,
          "t": 20,
          "u": 21,
          "v": 22,
          "w": 23,
          "x": 24,
          "y": 25,
          "z": 26,
          "A": 1 + 26,
          "B": 2 + 26,
          "C": 3 + 26,
          "D": 4 + 26,
          "E": 5 + 26,
          "F": 6 + 26,
          "G": 7 + 26,
          "H": 8 + 26,
          "I": 9 + 26,
          "J": 10 + 26,
          "K": 11 + 26,
          "L": 12 + 26,
          "M": 13 + 26,
          "N": 14 + 26,
          "O": 15 + 26,
          "P": 16 + 26,
          "Q": 17 + 26,
          "R": 18 + 26,
          "S": 19 + 26,
          "T": 20 + 26,
          "U": 21 + 26,
          "V": 22 + 26,
          "W": 23 + 26,
          "X": 24 + 26,
          "Y": 25 + 26,
          "Z": 26 + 26
          }

priorities_sum = 0

for rucksack in txt:
    left_side = rucksack[:len(rucksack) // 2]
    right_side = rucksack[len(rucksack) // 2:]
    print(f"left side: {left_side}")
    print(f"right side: {right_side}")

    i = 0
    while i <= len(left_side) - 1:
        j = 0
        while j <= len(right_side) - 1:
            if left_side[i] == right_side[j]:
                priority = values[left_side[i]]
                break
            j += 1
        i += 1
    priorities_sum += priority

print(priorities_sum)
    
