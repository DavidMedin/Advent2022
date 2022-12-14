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
        #l,r,u,d
        vis_row.append(0)
    map.append(row)
    vis.append(vis_row)

for yi,y in enumerate(map):
    for xi,x in enumerate(y):
        #split
        r_count = 0
        for ri in range(xi+1,len(y)):
            r_count+=1
            if map[yi][ri] >= x:
                break
        l_count = 0
        for li in range(xi-1,-1,-1):
            l_count+=1
            if map[yi][li] >= x:
                break
        u_count = 0
        for ui in range(yi+1,len(map)-1):
            u_count+=1
            if map[ui][xi] >= x:
                break;
        d_count = 0
        for di in range(yi-1,-1,-1):
            d_count+=1
            if map[di][xi] >= x:
                break

        total = r_count * l_count*u_count*d_count
        vis[yi][xi] = total

big = 0


for yi,y in enumerate(vis):
    for xi,x in enumerate(y):
        if x > big:
            big = x
print(big)