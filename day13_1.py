file = open("day13.data")
pck_p = []
tmp_pair = []
for line in file.readlines():
    real = line.split()
    if len(real) == 0:
        continue
    if len(tmp_pair) == 0:
        tmp_pair.append(eval(real[0]))
    else:
        tmp_pair.append(eval(real[0]))
        pck_p.append(tmp_pair)
        tmp_pair = []

def Cmp(pair):
    assert(type(pair) == list)
    assert(len(pair) == 2)
    for l,r in zip(pair[0],pair[1]):
        print(f"compare {l} to {r}")
        real_l,real_r = l,r
        if type(l) == int and type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
        if type(l) != type(r) :
            print("Converting to list")
            if type(real_l) == list:
                real_r = [r]
            else:
                assert(type(real_l) == int)
                real_l = [l]
            
        if type(real_l) == list and type(real_r) == list:
            res = Cmp([real_l,real_r])
            if res == None:
                continue
            return res
    if len(pair[1]) == len(pair[0]):
        return None
    return len(pair[0]) < len(pair[1])

works = 0
for pairi, pair in enumerate(pck_p):
    res = Cmp(pair)
    print(pairi+1,res)
    if res == True or res == None:
        works += pairi+1

print(works)