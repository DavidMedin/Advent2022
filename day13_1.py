file = open("day13.data")
pck_p = []
tmp_pair = []
for line in file.readlines():
    real = line.split()
    if len(real) == 0:
        continue
    # pair = []
    # pair.append(eval(line))
    # pair.append(eval(line))
    # pck_p.append(pair)
    if len(tmp_pair) == 0:
        tmp_pair.append(eval(real[0]))
    else:
        tmp_pair.append(eval(real[0]))
        pck_p.append(tmp_pair)
        tmp_pair = []

def Cmp(pair):
    for (l,r) in zip(pair[0],pair[1]):
        print(f"compare {l} to {r}")
        real_l,real_r = l,r
        if isinstance(l, int) and isinstance(r,int):
            if l < r:
                return True
            elif r < l:
                return False
        if isinstance(l,list) and isinstance(r,list):
            res = Cmp([l,r])
            if res == None:
                continue
            return res
        if isinstance(l,list) != isinstance(r,list) :
            print("Converting to list")
            if isinstance(l,list):
                real_r = [r]
            else:
                real_l = [l]
            res = Cmp([real_l,real_r])
            if res == None:
                continue
            return res

        
    if len(pair[1]) < len(pair[0]):
        return False
    return None

works = 0
for pairi, pair in enumerate(pck_p):
    res = Cmp(pair)
    print(pairi+1,res)
    if res == True or res == None:
        works += pairi+1

print(works)