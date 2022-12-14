file = open("day7.data")

class Node(object):
    # kind is 0 or 1, directory or file
    parent = None
    def __init__(self,name,kind,size=0):
        self.children = []
        self.kind = kind
        self.size = size
        self.name = name
    def add_child(self, node):
        if len ( list(filter(lambda x: x.name == node.name, self.children)) ) == 0:
            node.parent = self
            self.children.append(node)
root = Node("/",0)
current = root
for i, line in enumerate(file.readlines()):
    words = line.split()
    if line == "\n":
        continue
    if line[0] == "$":
        if words[1] == "cd":
            if words[2] == "..":
                current = current.parent
            elif words[2] != "/":
                matches = list(filter(lambda x: x.kind == 0 and x.name ==words[2], current.children))
                assert(len(matches) == 1)
                current = matches[0] # faith
    elif words[0] == "dir":
        current.add_child(Node(words[1],0))
    else:
        current.add_child( Node(words[1],1,int(words[0])) )


small = []
def recur(node):
    size = 0
    for file in node.children:
        if file.kind == 1:
            size += file.size
    for dir in node.children:
        if dir.kind == 0:
            size += recur(dir)
    node.size = size
    if size <= 100000:
        print(size)
        small.append(node)
    return size

recur(root)