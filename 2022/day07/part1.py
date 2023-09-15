with open("input.txt", "r") as file:
    txt = file.read().strip().split("\n")

# txt = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k""".split("\n")

class Folder():
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.contents = []

    def get_size(self):
        return sum([item.get_size() for item in self.contents])

class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

curr_folder = Folder("/")
all_folders = [curr_folder]

for line in txt:
    command = line.split(" ")

    if command[0] == "$" and command[1] == "cd":
        if command[2] == "..":
            curr_folder = curr_folder.parent
        else:
            for item in curr_folder.contents:
                if item.name == command[2] and type(item) == Folder:
                    curr_folder = item
    
    elif command[0] == "$" and command[1] == "ls":
        pass

    elif command[0] == "dir":
        new_folder = Folder(command[1])
        all_folders.append(new_folder)
        new_folder.parent = curr_folder
        curr_folder.contents.append(new_folder)
    
    else:
        curr_folder.contents.append(File(command[1], int(command[0])))

part1 = 0

for folder in all_folders:
    print(folder.name)
    if folder.get_size() <= 100_000:
        part1 += folder.get_size()
        print(folder.name, folder.get_size())


print(part1)