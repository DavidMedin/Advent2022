file = open("day10.data")
cpu = 1
x_reg = 1

lines = [ ['.']*40 ]
vert = 0
laser = 0
def NextCycle():
    global cpu
    global x_reg
    global lines
    global vert
    global laser

    # update CRT
    if x_reg-1 <= laser <= x_reg+1:
        lines[vert][laser] = "#"
    laser += 1
    if laser == 40:
        lines.append(["."]*40)
        vert += 1
        laser = 0
    
    cpu += 1

def Render():
    for rowi,row in enumerate(lines):
        for xi,x in enumerate(row):
            print(x,end="")
        print(" ")

for line in file.readlines():
    words = line.split()
    if words[0] == "noop":
        NextCycle()
    elif words[0] == "addx":
        for i in range(2):
            NextCycle()
        x_reg += int(words[1])
Render()