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

@ignore_unhashable
@functools.lru_cache
#                     (target,dist)
def dfs(node,elephant, node_quest, ele_quest, gain, time,visited,ele_last=None,last=None):
    if time <= 0:
        return 0
    node_i = get_index(node.name)
    elephant_i = get_index(elephant.name)
    scores = [gain]


    # If I turn it on:
    #     For ele's neighbors'

    #     If ele turns it on (instead)
    
    # If I don't it on
    #     For ele's neighbors'

    #     If ele turns it on (instead)

    # If I turn it on, ele doesn't

    if node_quest == None and visited[node_i] == False and node.rate != 0:
        visit_copy = list(visited)
        visit_copy[node_i] = True

        # finish or continue the quest
        can_continue = True
        if ele_quest != None:
            if ele_quest[1] == 0:
                # the quest is complete
                elephant = ele_quest[0]
                ele_quest = None
            else:
                #Continue the quest
                scores.append( dfs(node, elephant,None,(ele_quest[0], ele_quest[1]-1), gain + node.rate * (time-1) , time - 1, list (visit_copy) ,elephant,node )  )
                can_continue = False
        if can_continue:
            for (ele_index, dist) in elephant.real_neighs:
                ele_obj = valves[ele_index]

                # Don't go backwards!
                if ele_last != elephant and ele_obj == ele_last:
                    continue

                scores.append( dfs(node, elephant,None,(ele_obj, dist-1), gain + node.rate * (time-1) , time - 1, list (visit_copy) ,elephant,node )  )
    
    # What if we both turn it on?
    if ele_quest == None and node_quest == None and node != elephant and node.rate != 0 and elephant.rate != 0 and node_quest == None and ele_quest == None and visited[node_i] == False and visited[elephant_i] == False:
        visit_copy = list(visited)
        visit_copy[node_i] = True
        visit_copy[elephant_i] = True
        scores.append( dfs(node,elephant, None, None , gain + (node.rate + elephant.rate) * (time-1), time - 1, visit_copy,elephant,node )  )
    

    # Continue or complete my quest
    can_continue = True
    if node_quest != None:
        if node_quest[1] == 0:
            # the quest is complete
            node = node_quest[0]
            node_quest = None
        else:
            #Continue the quest

            # if the elephant can turn it on
            if  ele_quest == None and visited[elephant_i] == False and elephant.rate != 0:
                visit_copy = list(visited)
                visit_copy[elephant_i] = True
                scores.append( dfs(obj, elephant, gain + elephant.rate * (time-1) , time - 1, visit_copy ,elephant,node )  )
            
            # what if it didn't?
            for ele_neigh in elephant.neighs:
                ele_obj = get_valve(ele_neigh)

                # Don't go backwards!
                if ele_last != elephant and ele_obj == ele_last:
                    continue

                scores.append( dfs(obj, ele_obj, gain, time - 1, list(visited) ,elephant,node )  )

            scores.append( dfs(node, elephant,(node_quest[0], node_quest[1]-1),None, gain + node.rate * (time-1) , time - 1, list (visit_copy) ,elephant,node )  )
            can_continue = False

    if can_continue:
        # if I do not turn this one on
        for (node_index, node_dist) in node.real_neigh:
            obj = valves[node_index]
            # Don't go backwards!
            if last != node and obj == last:
                continue

            # if the elephant can turn it on
            if  ele_quest == None and visited[elephant_i] == False and elephant.rate != 0:
                visit_copy = list(visited)
                visit_copy[elephant_i] = True
                scores.append( dfs(obj, elephant, gain + elephant.rate * (time-1) , time - 1, visit_copy ,elephant,node )  )
            
            # what if it didn't?
            for ele_neigh in elephant.neighs:
                ele_obj = get_valve(ele_neigh)

                # Don't go backwards!
                if ele_last != elephant and ele_obj == ele_last:
                    continue

                scores.append( dfs(obj, ele_obj, gain, time - 1, list(visited) ,elephant,node )  )

    the_max = max(scores)
    return the_max

for valve in valves:
    if valve.name == "AA":
        print(dfs(valve,valve, 0,26, [False] * len(valves) ))
        break