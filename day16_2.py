import re
import functools
findall = lambda s: [int(x) for x in re.findall(r'-?\d+',s)]
def ignore_unhashable(func): 
    uncached = func.__wrapped__
    attributes = functools.WRAPPER_ASSIGNMENTS + ('cache_info', 'cache_clear')
    @functools.wraps(func, assigned=attributes) 
    def wrapper(*args, **kwargs): 
        try: 
            return func(*args, **kwargs) 
        except TypeError as error: 
            if 'unhashable type' in str(error): 
                return uncached(*args, **kwargs) 
            raise 
    wrapper.__uncached__ = uncached
    return wrapper


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

@ignore_unhashable
@functools.lru_cache
def get_valve(name):
    global valves
    for valve in valves:
        if valve.name == name:
            return valve
    assert(False)

@ignore_unhashable
@functools.lru_cache
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

def check_legal(hist1,hist2):
    pass
#                     (target,dist)
def dfs(node,elephant, node_quest, elephant_quest, gain, time,visited, hist=[],ele_hist=[]):
    if time <= 0:
        return 0
    node_i = get_index(node.name)
    elephant_i = get_index(elephant.name)
    scores = [gain]

    def do_elephant(node_target):
        if elephant_quest != None:
            # continue it
            if elephant_quest[1] == 0:
                # done with the quest
                elephant = elephant_quest[0]
                elephant_quest = None
                do_elephant()
            else:
                elephant_quest[1] -= 1
                if node_target == None:
                    # node is opening a valve
                    visited_copy = list(visited)
                    visited_copy[get_index(node_target[0])] = True

                    hist_copy = list(hist)
                    hist_copy.append(node_target[0].name)
                    scores.append ( dfs(node,elephant,None,elephant_quest, gain + node_target[0].rate * (time-1), time-1,visited_copy,hist_copy,list(ele_hist)) )
                else:
                    # node is opening a valve
                    visited_copy = list(visited)

                    hist_copy = list(hist)
                    scores.append ( dfs(node,elephant,None,elephant_quest, gain + node_target[0].rate * (time-1), time-1,visited_copy,hist_copy,list(ele_hist)) )
        else:
            for ele_neigh in elephant.neighs:
                pass

    if node_quest != None:
        do_elephant()
    else:
        for neigh in node.neighs:
            
            do_elephant()
    
    # what if I opened a valve?
    do_elephant()
    ## ===============
    # if visited[node_i] == False and node.rate != 0:
    #     for ele_neigh in elephant.neighs:
    #         ele_obj = get_valve(ele_neigh)

    #         # Don't go backwards!
    #         if ele_last != elephant and ele_obj == ele_last:
    #             continue

    #         visit_copy = list(visited)
    #         visit_copy[node_i] = True
    #         scores.append( dfs(node, ele_obj, gain + node.rate * (time-1) , time - 1, visit_copy ,elephant,node )  )
    
    # # What if we both turn it on?
    # if node != elephant and node.rate != 0 and elephant.rate != 0 and visited[node_i] == False and visited[elephant_i] == False:
    #     visit_copy = list(visited)
    #     visit_copy[node_i] = True
    #     visit_copy[elephant_i] = True
    #     scores.append( dfs(node,elephant, gain + (node.rate + elephant.rate) * (time-1), time - 1, visit_copy,elephant,node )  )
    
    # # if I do not turn this one on
    # for my_neigh in node.neighs:
    #     obj = get_valve(my_neigh)
    #     # Don't go backwards!
    #     if last != node and obj == last:
    #         continue

    #     # if the elephant can turn it on
    #     if visited[elephant_i] == False and elephant.rate != 0:
    #         visit_copy = list(visited)
    #         visit_copy[elephant_i] = True
    #         scores.append( dfs(obj, elephant, gain + elephant.rate * (time-1) , time - 1, visit_copy ,elephant,node )  )
        
    #     # what if it didn't?
    #     for ele_neigh in elephant.neighs:
    #         ele_obj = get_valve(ele_neigh)

    #         # Don't go backwards!
    #         if ele_last != elephant and ele_obj == ele_last:
    #             continue

    #         scores.append( dfs(obj, ele_obj, gain, time - 1, list(visited) ,elephant,node )  )

    the_max = max(scores)
    return the_max

for valve in valves:
    if valve.name == "AA":
        print(dfs(valve,valve, 0,26, [False] * len(valves) ))
        break