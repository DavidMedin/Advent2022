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


def dfs_neighbors(node, dist, visited,neighbors):
    visited[get_index(node.name)] = True
    for neigh in node.neighs:
        if visited[get_index(neigh)] == True:
            continue
        obj = get_valve(neigh)
        if obj.rate != 0:
            neighbors.append((get_index(neigh), dist+1))
            continue
        dfs_neighbors(obj, dist+1, visited,neighbors)

for valve in valves:
    neighbors = []
    dfs_neighbors(valve, 0, [False] * len(valves),neighbors)
    valve.real_neigh = neighbors

def dfs(node, gain, time,visited, history,last=None):
    if time <= 0:
        return 0,history
    node_i = get_index(node.name)
    scores = []

    opened = False

    if node.rate != 0 and visited[node_i] == False:
        for (neigh, dist) in node.real_neigh:
            if dist >= time:
                continue
            obj = valves[neigh]
            if obj == last: # Didn't open this valve, don't go backwards
                continue 
            new_hist = history.copy()
            new_hist.append(obj.name)
            scores.append( dfs(obj, gain, time - dist, visited.copy(), new_hist,node )  )
        
        visited[node_i] = True
        time -= 1
        gain += time * node.rate
        history.append(f"Open {node.name}")
        opened = True

    for (neigh, dist) in node.real_neigh:
        if dist >= time:
            continue
        obj = valves[neigh]
        if opened == False and obj == last:
            continue
        new_hist = history.copy()
        new_hist.append(obj.name)
        scores.append( dfs(obj, gain, time - dist, visited.copy(), new_hist,node )  )
    if len(scores) == 0:
        return gain,history
    the_max = max(scores, key=lambda x: x[0])
    return the_max

# print(dfs(valves[0], 0,30, [False] * len(valves), [] ))
for valve in valves:
    if valve.name == "AA":
        print(dfs(valve, 0,26, [False] * len(valves), [] ))
        break