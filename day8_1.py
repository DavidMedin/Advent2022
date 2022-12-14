file = open("day8.data")
map = []
vis = []
for line in file.readlines():
    row = []
    vis_row = []
    for char in line:
        if(char == "\n"):
            continue
        row.append(int(char))
        vis_row.append(False)
    map.append(row)
    vis.append(vis_row)

top_max = [-1] * len(map)
bot_max = [-1] * len(map)
for yi,y in enumerate(map):
    max_x = -1
    for xi,x in enumerate(y):
        if x > max_x:
            max_x = x
            vis[yi][xi] = True
        if x > top_max[xi]:
            top_max[xi] = x
            vis[yi][xi] = True
    
    max_x = -1
    for xi,x in enumerate(reversed(y)):
        if x > max_x:
            max_x = x
            vis[yi][len(y) - 1- xi] = True

for yi,y in enumerate(reversed(map)):
    for xi,x in enumerate(y):
        if x > bot_max[xi]:
            bot_max[xi] = x
            vis[len(map) - 1 -yi][xi] = True

count = 0
for y in vis:
    for x in y:
        if x == True:
            count += 1
print(count)