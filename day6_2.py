file = open("day6.data","r")
for line in file.readlines():
    # one line
    for i in range(len(line) - 4):
        let_arr = []
        for x in range(14):
            let_arr.append(line[i+x])
        char_set = set(let_arr)
        if len(char_set) == 14:
            print(i+14)
            break