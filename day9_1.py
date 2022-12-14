file = open("day9.data")
tail_visit = []
size = 1600
for i in range(size):
    tail_visit.append([False] * size)
knots = [[int(size/2),int(size/2)] for _ in range(10) ]
tail_visit[knots[9][1]][knots[9][0]] = True
def is_satisfied(knot1,knot2):
    return abs(knot1[0] - knot2[0]) <= 1 and abs(knot1[1] - knot2[1]) <= 1

def print_map():
    print("\n\n\n======================\n\n\n")
    for rowi,row in enumerate((tail_visit)):
        for xi,x in enumerate((row)):
            val = None
            
            if x == True:
                val = 't'
            else:
                val = '.'
                for knoti, knot in enumerate(knots):
                    if xi == knot[0] and rowi == knot[1]:
                        val = str(knoti)
            
            
            if xi == int(size/2) and rowi == int(size/2):
                val = "S"
            print(val + " ",end = "")
        print(" ")
    print("\n")


def satisfy(headi,taili):
    head = knots[headi]
    tail = knots[taili]
    if is_satisfied(head,tail) == False:
        if head[0] == tail[0]:
            if head[1] > tail[1]:
                tail[1] += 1
            elif head[1] < tail[1]:
                tail[1]-= 1
            
        elif head[1] == tail[1]:
            if head[0] > tail[0]:
                tail[0] += 1
            elif head[0] < tail[0]:
                tail[0] -= 1

        else:
            # diagonal
            if head[0] > tail[0]:
                tail[0]+= 1
            if head[0] < tail[0]:
                tail[0] -= 1
            if head[1] > tail[1]:
                tail[1] += 1
            if head[1] < tail[1]:
                tail[1] -= 1

    if taili+1 == len(knots):
        return
    while is_satisfied(knots[taili], knots[taili+1]) == False:
        satisfy(taili, taili+1)
        if taili+1 == 9:
            tail_visit[knots[9][1]][knots[9][0]] = True

# print_map()

for line in file.readlines():
    words = line.split()
    amount = int(words[1])
    index = 0
    dir = 1
    match words[0]:
        case "D":
            index = 1
        case "U":
            index = 1
            dir = -1
        case "L":
            dir = -1
            index = 0
        case "R":
            index = 0

    while amount != 0:
        knots[0][index] += 1 * dir
        while is_satisfied(knots[0],knots[1]) == False:
            satisfy(0,1)
        #     print_map()
        # else:
        #     print_map()
        amount -= 1
        
        

# print(tail_visit)
sum = 0
max = 0
for rowi,row in enumerate(tail_visit):
    for xi, i in enumerate(row):
        if i == True:
            if xi > max:
                max = xi
            sum += 1
print(max)
print(sum)