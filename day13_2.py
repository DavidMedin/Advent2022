import functools
file = open("day13.data")
pkgs  = []
pck_p = []
tmp_pair = []
for line in file.readlines():
    real = line.split()
    if len(real) == 0:
        continue
    pkgs.append(eval(real[0]))
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
        # print(f"compare {l} to {r}")
        real_l,real_r = l,r
        if type(l) == int and type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
        if type(l) != type(r) :
            # print("Converting to list")
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

def uh(x,y):
    # return Cmp([y,x]) == True or Cmp([y,x]) == None
    res = Cmp([x,y])
    if res == True:
        return -1
    if res == False:
        return 1
    return 0

# pkg_sort = sorted(pkgs, key=uh)
pkgs.insert(1,[[6]])
pkgs.insert(1,[[2]])
pkgs.sort(key=functools.cmp_to_key(uh))

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)


works = 0
for pairi, pair in enumerate(pairwise(pkgs)):
    res = Cmp([pair[0],pair[1]])
    # print(pairi+1,res)
    if res == True or res == None:
        works += pairi+1

# copy = pkgs.copy()
first = False

# print(works)

# dug = 0
# for i,pkg in enumerate(pkgs):
#     res = Cmp([pkg,[[2]] ])
#     if first == False:
#         # copy.insert(i, [[2]])
#         first = True
#         print(f"Found first {i+1}")
#         dug += i+1
    
#     res = Cmp([pkg,[[6]] ])
#     if res == False:
#         print(f"found second {i+2}")
#         # copy.insert(i, [[6]])
#         dug *= i+2
#         break

print((pkgs.index([[6]])+1) * (pkgs.index([[2]])+1))