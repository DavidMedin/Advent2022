file = open("day5.data",'r')
stacks = [['T','P','Z','C','S','L','Q','N'],['L','P','T','V','H','C','G'],['D','C','Z','F'],['G','W','T','D','L','M','V','C'],['P','W','C'],['P','F','J','D','C','T','S','Z'],['V','W','G','B','D'],['N','J','S','Q','H','W'],['R','C','Q','F','S','L','V']]
print(len(stacks))
for line in file.readlines():
    if line[0] == 'm':
        nums = [int(i) for i in line.split() if i.isdigit()]
        mount = nums[0]
        pick = []
        for i in range(mount):
            get = stacks[nums[1]-1].pop()
            pick.append(get)
        pick.reverse()
        for i in pick:
            stacks[nums[2]-1].append(i)
for stack in stacks:
    print(stack.pop())