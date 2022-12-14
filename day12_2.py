import math
import sys
sys.setrecursionlimit(11000)
file = open("day12.data")
h_map = []
you = [0,0]
target = [0,0]
for linei, line in enumerate(file.readlines()):
    this_line = list(line.split()[0])
    this_line
    for xi,x in enumerate(this_line):
        if x == 'S':
            target = [linei,xi]
            this_line[xi] = 'a'
        elif x == 'E':
            you = [linei,xi]
            this_line[xi] = 'z'
    h_map.append(this_line)

# visited = [[0] * len(h_map[0])] * len(h_map)
visited = []
for y in range(len(h_map)):
    visited.append([])
    for x in range(len(h_map[0])):
        visited[y].append(0)
c = 0

def Search(where, count=0):
    global c
    cost = visited[where[0]][where[1]]

    # check for map bounds
    # if 0 <= where[0]-1 and visited[where[0]-1][where[1]] == False:
    #     Search([where[0]-1,where[1]])
    # if where[0]+1 < len(visited[1]) and visited[where[0]+1][where[1]] == False:
    #     Search([where[0]+1,where[1]])

    # if 0 <= where[1]-1 and visited[where[0]][where[1]-1] == False:
    #     Search([where[0],where[1]-1])
    # if where[1]+1 < len(visited) and visited[where[0]][where[1]+1] == False:
    #     Search([where[0],where[1]+1])

    dirs = [[where[0]-1,where[1]],[where[0]+1,where[1]],[where[0],where[1]-1],[where[0],where[1]+1]]
    # dirs = sorted(dirs, key=lambda x: math.dist(x,target) )
    lengths = []
    for diri, dir in enumerate(dirs):
        # if dir == where:
        #     continue
        if 0 <= dir[0] < len(visited) and 0 <= dir[1] < len(visited[0]):
            if ord(h_map[where[0]][where[1]])-ord(h_map[dir[0]][dir[1]]) > 1:
                continue # too tall
            if h_map[dir[0]][dir[1]] == 'a':
                # lengths.append(cost+1)
                # continue # found it!
                return cost+1
            
            if visited[dir[0]][dir[1]] == 0 or cost+1 < visited[dir[0]][dir[1]]:
                visited[dir[0]][dir[1]] = cost + 1
                res = Search(dir, count+1)
                c += 1
                if res != False:
                    lengths.append(res)
    if len(lengths)== 0:
        return False
    else:
        lengths.sort()
        return lengths[0]

print(Search(you))
nother = []
for y in range(len(h_map)):
    nother.append([])
    for x in range(len(h_map[0])):
        nother[y].append([h_map[y][x],visited[y][x]])
print("yoo")
# for line in h_map:
#     for x in line:
#         print(x,end="")
#     print()