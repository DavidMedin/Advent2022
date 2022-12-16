import pandas as pd
import piso
import re
import threading
# from tqdm import tqdm
file = open("day15.data")
findall = lambda s: [int(x) for x in re.findall(r'-?\d+',s)]
manhat = lambda a,b: abs(a[0]-b[0]) + abs(a[1]-b[1])

size = 4000001

inputs = []

for line in file.readlines():
    num = findall(line)
    sensor = [num[0],num[1]]
    beacon = [num[2],num[3]]
    dist = manhat(sensor , beacon)
    diamond = {
        sensor[1] : pd.Interval(left=sensor[0]-dist, right=sensor[0]+dist, closed="both")
    }
    # go up
    print(dist)
    for i in range(dist):
        diamond[sensor[1] - (i + 1)] = pd.Interval(left=sensor[0]-dist+(i+1)-1, right=sensor[0]+dist-(i+1), closed="both")
        diamond[sensor[1] + (i + 1)] = pd.Interval(left=sensor[0]-dist+(i+1)-1, right=sensor[0]+dist-(i+1), closed="both")
    inputs.append(diamond)

def do_a_lot(start,end):
    local_data = threading.local()
    for depth in range(start,end+1):
        local_data.relevent = []
        for input in inputs:
            if depth in input:
                interval = input[depth]
                if interval.overlaps( pd.Interval(0,size-1, closed="both") ):
                    local_data.relevent.append(interval)
        inter_array = pd.arrays.IntervalArray(local_data.relevent,closed="right")
        # get the union of them all
        unions = piso.union( inter_array )
        if len(unions) != 1:
            print("found it!") 
            for x in range(size):
                if not( x in unions[0] ) and not (x in unions[1] ):
                    # this is not in either
                    print(x*4000000 + depth)
                    exit()
        if depth % 1000 == 0:
            print("done with depth ", depth)

threads = []
count = 10
for i in range(count):
    threads.append(threading.Thread(target=do_a_lot, args=[i*int(size/count),(i+1)*int(size/count)-1]))
    print([i*int(size/count),(i+1)*int(size/count)-1])
for thread in threads:
    thread.start()
