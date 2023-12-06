
import os
from treelib import Node, Tree

class File(object):
        def __init__(self, size, isFile):
            self.size= size
            self.isFile=isFile
dirtree = Tree()
position=0
def changeDir(name):
    if name=="/":
        return 0
    elif name=="..":
        node=dirtree.get_node(position)
        return dirtree.parent(node.identifier).identifier
    else:
        childs=dirtree.children(position)
        for c in childs:
            if c.tag==name:
                return c.identifier
#inputFile='./day7/sample.txt'
#inputFile='input.txt'
inputFile='sample.txt'
id=0
#Read file and populate tree
with open(inputFile) as f:
    dirtree.create_node("/",0,data=File(0,True))
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
            dirtree.create_node(dirname,id,parent=position,data=File(0,False))
            id+=1
        if l.split(" ")[0].isnumeric():
            fileName=l.split(" ")[-1]
            dirtree.create_node(fileName,id,parent=position,data=File(int(l.split(" ")[0]),True))
            id+=1
dirtree.show()
for node in dirtree.all_nodes_itr():
    if node.data.isFile:
        print(node)
        print(node.is_leaf())
    #if node.identifier==len(dirtree)-1:
    #    break