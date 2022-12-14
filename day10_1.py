file = open("day10.data")
cpu = 1
x_reg = 1

width = 40
height = 6

signal = 0
def NextCycle():
    global cpu
    global x_reg
    global signal
    if cpu == 20:
        # print("20 * ", x_reg)
        signal += 20 * x_reg
    if cpu > 20 and (cpu-20) % 40 == 0:
        # print(f"{cpu} * {x_reg}")
        signal += cpu * x_reg
    cpu += 1

for line in file.readlines():
    words = line.split()
    if words[0] == "noop":
        NextCycle()
    elif words[0] == "addx":
        for i in range(2):
            NextCycle()
        x_reg += int(words[1])
print(signal)