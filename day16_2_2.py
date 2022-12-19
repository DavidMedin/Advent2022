import re
findall = lambda s: [int(x) for x in re.findall(r'-?\d+',s)]

class Valve:
    def __init__(self, name,rate, neighbors):
        self.name = name
        self.rate = rate
        self.neighs = neighbors
        self.shortest = -1

valves = []

file = open("day16.data")

for line in file.readlines():
    words = line.split()
    valve = words[1]
    rate = findall(line)[0]

    leads_to = []
    for word in reversed(words):
        if word == "valve" or word == "valves":
            break
        leads_to.append(word.split(",")[0])
    valves.append(Valve(valve,rate, leads_to))

def get_valve(name):
    global valves
    for valve in valves:
        if valve.name == name:
            return valve
    assert(False)

def get_index(name):
    global valves
    for i,valve in enumerate(valves):
        if valve.name == name:
            return i
    assert(False)


## Floyd Warshall
nV = len(valves)

INF = 999


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance
# G = [[0, 3, INF, 5],
#          [2, 0, INF, 4],
#          [INF, 1, 0, INF],
#          [INF, INF, 2, 0]]
G = []
for valve1 in valves:
    row = []
    for valve2 in valves:
        for neigh in valve2.neighs:
            if valve1.name == neigh:
                row.append(1)
                break
        else:
            row.append(INF)
    G.append(row)

G = floyd_warshall(G)


# def dfs_neighbors(node, dist, visited,neighbors):
#     visited[get_index(node.name)] = True


# for valve in valves:
#     neighbors = []
#     dfs_neighbors(valve, 0, [False] * len(valves),neighbors)
#     valve.real_neigh = neighbors

all_combos = []

def dfs(node, time,visited, history):
    global all_combos
    if time <= 1:
        return
    node_i = get_index(node.name)

    # opened = False

    # if :
        # for (neigh, dist) in node.real_neigh:
        #     if dist >= time:
        #         continue
        #     obj = valves[neigh]
        #     if obj == last: # Didn't open this valve, don't go backwards
        #         continue 
        #     new_hist = dict(history)
        #     dfs(obj, time - dist, list(visited), new_hist,node )
        
        # visited[node_i] = True
        # time -= 1
        # history[time] = node.name
        # all_combos.append( dict(history) )
        # opened = True

    for obj in valves:
        if obj == node or obj.rate == 0: continue
        obj_i = get_index(obj.name)
        dist = G[obj_i][node_i]
        if dist+1 >= time:
            continue
        if obj.rate != 0 and visited[obj_i] == False:
            new_visit = list(visited)
            new_hist = dict(history)
            new_visit[obj_i] = True
            new_hist[time - (dist + 1)] = obj.name
            all_combos.append( dict(new_hist) )
            dfs(obj, time - (dist + 1),new_visit , new_hist )

max_time = 26
for valve in valves:
    if valve.name == "AA":
        dfs(valve,max_time, [False] * len(valves), {} )
        break

def get_score(comb1,comb2):
    for k,v in comb1.items():
        for k2,v2 in comb2.items():
            if v == v2:
                # return (0,{},{})
                return 0
    
    gain = 0
    for k,v in comb1.items():
        obj = get_valve(v)
        gain += k * obj.rate
    for k,v in comb2.items():
        obj = get_valve(v)
        gain += k * obj.rate
    return gain

print(len(all_combos))
print("computing...")
scores = []

curr_max = 0
for i,comb1 in enumerate(all_combos):
    if i % 10 == 0:
        print(i)
    for comb2 in all_combos:
        val = get_score(comb1,comb2)
        if val > curr_max:
            curr_max = val
print("Done!")
print(curr_max)