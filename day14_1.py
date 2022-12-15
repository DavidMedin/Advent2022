world = []
for i in range(600):
    row = []
    for x in range(600):
        row.append(".")
    world.append(row)

def DrawLine(p1,p2):
    if(p1[0] > p2[0]):
        for x in range(p1[0],p2[0]-1,-1):
            world[p1[1]][x] = "#"
    else:
        for x in range(p1[0],p2[0]+1):
            world[p1[1]][x] = "#"

    if p1[1] > p2[1]:
        for y in range(p1[1],p2[1]-1,-1):
            world[y][p1[0]] = "#"
    else:
        for y in range(p1[1],p2[1]+1):
            world[y][p1[0]] = "#"


file = open("day14.data")
for line in file.readlines():
    words = line.split()
    last_p = list( map(int, words[0].split(",")) )
    for word in words:
        if word == "->":
            continue
        DrawLine(last_p,list( map(int, word.split(",")) ))
        last_p = list( map(int, word.split(",")) )


sands = 0
done = True
while(done):
    # sand
    sand = [500,0]
    while(True):
        if sand[1]+1 >= len(world):
            done = False
            break
        if world[sand[1]+1][sand[0]] == '.':
            # move down
            sand[1] += 1
        elif world[sand[1]+1][sand[0]-1] == '.':
            sand[1] += 1
            sand[0] -= 1
        elif world[sand[1]+1][sand[0]+1] == '.':
            sand[1] += 1
            sand[0] += 1
        else:
            world[sand[1]][sand[0]] = "o"
            sands += 1
            print(sands)
            break
print(sands)