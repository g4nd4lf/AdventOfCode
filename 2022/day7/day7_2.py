
import os
from anytree import Node, RenderTree, AsciiStyle, PostOrderIter

class File(object):
        def __init__(self, size, isFile):
            self.size= size
            self.isFile=isFile
#dirtree = Tree()
position=0
def changeDir(name):
    if name=="/":
        return 0
    elif name=="..":
        node=dirtree[position]
        return node.parent.pos
    else:
        childs=dirtree[position].children
        for c in childs:
            if c.name==name:
                return c.pos
#inputFile='./day7/sample.txt'
inputFile='input.txt'
#inputFile='sample.txt'
id=0
#Read file and populate tree
dirtree=[]
with open(inputFile) as f:
    dirtree.append(Node("root",pos=id,data=File(0,True)))
    id+=1
    #lines = f.readlines()
    lines = f.read().splitlines()
    position=dirtree
    for l in lines:
        if "$ cd" in l:
            position=changeDir(l.split(" ")[-1])            
        if "$ ls" in l:
            continue
        if "dir " in l:
            dirname=l.split(" ")[-1]
            dirtree.append(Node(dirname,pos=id,parent=dirtree[position],data=File(0,False)))
            id+=1
        if l.split(" ")[0].isnumeric():
            fileName=l.split(" ")[-1]
            dirtree.append(Node(fileName,pos=id,parent=dirtree[position],data=File(int(l.split(" ")[0]),True)))
            id+=1
print(RenderTree(dirtree[0],style=AsciiStyle()).by_attr())
for node in PostOrderIter(dirtree[0]):
    #print(node.name+": "+str(node.data.size))
    if node.parent:
        node.parent.data.size+=node.data.size
total=0
for node in PostOrderIter(dirtree[0]):
    if (not node.data.isFile) and node.data.size <= 100000:
        print(node.name+": "+str(node.data.size))
        total+=node.data.size
    #node.parent.data["size"]+=node.data["size"]
bigDirs=[]
for node in PostOrderIter(dirtree[0]):
    if (not node.data.isFile) and node.data.size >= 8748071:
        print(node.name+": "+str(node.data.size))
        bigDirs.append(node.data.size)
        #total+=node.data.size
solution=min(bigDirs)
print(solution)

