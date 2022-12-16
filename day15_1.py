
import re
import math
file = open("day15.data")
findall = lambda s: [int(x) for x in re.findall(r'-?\d+',s)]
manhat = lambda a,b: abs(a[0]-b[0]) + abs(a[1]-b[1])

depth = 2000000 # y
size = 12000000
target_line = ["."] * size
offset = int(-(size/2))
# offset = -4

for line in file.readlines():
    num = findall(line)
    # print(num)
    sensor = [num[0],num[1]]
    beacon = [num[2],num[3]]
    dist = manhat(sensor , [num[2],num[3]])
    for i,v in enumerate(target_line):
        if manhat(sensor, [i+offset, depth]) <= dist:
            target_line[i] = "#"
    print(sensor[0],offset,sensor[0]-offset, sensor[0]-offset > 0)
    if sensor[1] == depth:
        target_line[sensor[0]-offset] = "S"
    if beacon[1] == depth:
        target_line[beacon[0]-offset] = "B"

count = 0
for v in target_line:
    if v == "#":
        count += 1
print(count)