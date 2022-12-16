import re
import numpy as np
findall = lambda s: [int(x) for x in re.findall(r'-?\d+',s)]

class Valve:
    def __init__(self, name,rate, neighbors) -> None:
        self.name = name
        self.rate = rate
        self.neighs = neighbors
        self.open = False
        self.shortest = -1

valves = []
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

def shortest(start,end,dist=0):
    start.shortest = dist+1
    dists = []
    for neigh in start.neighs:
        if neigh == end.name:
            return dist+1
        neigh_obj = get_valve(neigh)
        if neigh_obj.shortest != -1 and neigh_obj.shortest <= dist+1:
            continue
        res = shortest(neigh_obj,end,dist+1)
        if res != None:
            dists.append(res)
    dists.sort(reverse=True)
    if len(dists) == 0:
        return None
    return dists[0]

def reset():
    global valves
    for valve in valves:
        valve.shortest = -1

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


def dfs_neighbors(node, dist, visited):
    neighs = []
    visited[get_index(node.name)] = True
    for neigh in node.neighs:
        if visited[get_index(neigh)] == True:
            continue
        neigh_obj = get_valve(neigh)
        if neigh_obj.rate != 0:
            neighs.append((dist+1, get_index(neigh)))
            continue
        wack =dfs_neighbors(neigh_obj, dist+1,visited)
        if len(neighs) == 0:
            neighs = wack
        else:
            np.concatenate((neighs, wack))
    return neighs

for valve in valves:
    valve.real_neigh = dfs_neighbors(valve, 0, [False] * len(valves))

current = valves[0]

relief = 0
acc_flow = 0
time = 30
visited_valves = 0
def do_time():
    global relief, acc_flow,time
    print(f"Done with {30-time+1}, rate : {acc_flow}")
    relief += acc_flow
    time -= 1

def score(start,target,time):
    if target.open == True or target.rate == 0:
        return 99999
    dist = shortest(start,target) + 1
    reset()
    if time <= dist:
        return 99999
    # score = target.rate * (time - dist)
    # for valve in valves:
    #     if valve == target: continue
    #     score += valve.rate / shortest(target,valve)
    #     reset()
    # print(score)
    return dist+1

# while time > 0:
#     if visited_valves == len(valves):
#         break

#     target_valve = sorted(valves, key=lambda x: score(current,x,time))[0]
#     if target_valve.rate == 0:
#         break
#     dist = shortest(current,target_valve)
#     reset()
#     print(f"Target : {target_valve.name}, dist : {dist}, flow : {target_valve.rate}")
#     current = target_valve

#     if dist+1 >= time: break
#     for i in range(dist+1):
#         do_time()
#     acc_flow += target_valve.rate
#     target_valve.open = True
#     visited_valves += 1

# while time > 0:
#     do_time()

# print(relief)

def dfs(node,time,flow, gain,visited):
    if time <= 0:
        return gain
    node_index = get_index(node.name)

    # gain += flow
    if visited[node_index] == False and  node.rate > 0:
        visited[node_index] = True
        flow += node.rate
        time -= 1
    scores = []
    for (dist_to,neigh_i) in node.real_neigh:
        # if visited[get_index(neigh)] == True:
        #     continue
        neigh_obj = valves[neigh_i]
        if time-dist_to <= 0:
            continue
        scores.append(dfs(neigh_obj, time-dist_to, flow, gain + flow * dist_to, visited.copy()))
    if len(scores) == 0:
        return gain
    return max(scores)

print(dfs(valves[0], 30,0,0 , [False] * len(valves)))

# sorted_valves = sorted(valves, key=lambda x: x.rate, reverse=True)
# for valve in sorted_valves:
#     best_match = sorted()
#iterate through all nodes, sorted descending by flow rate
#compare potential gain for the rest of time
#go to the best gain point