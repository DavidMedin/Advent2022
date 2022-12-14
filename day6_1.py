file = open("day6.data","r")
for line in file.readlines():
    # one line
    for i in range(len(line) - 3):
        char_set = set([line[i],line[i+1],line[i+2],line[i+3]])
        if len(char_set) == 4:
            print(i+4)
            break