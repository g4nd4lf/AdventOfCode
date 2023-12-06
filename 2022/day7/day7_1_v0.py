
import os

class Tree(object):
    def __init__(self, data, children=None, parent=None):
        self.data = data
        self.children = children or []
        self.parent = parent

    def add_child(self, data):
        new_child = Tree(data, parent=self)
        self.children.append(new_child)
        return new_child

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.children

    def __str__(self):
        if self.is_leaf():
            return str(self.data)
        return '{data} [{children}]'.format(data=self.data, children=', '.join(map(str, self.children)))

#input1='./day2/sample.txt'
#inputFile='input.txt'
inputFile='sample.txt'

#Read file and populate tree
with open(inputFile) as f:
    dirs=[]
    #lines = f.readlines()
    lines = f.read().splitlines()
    dirtree=Tree("/")
    position=dirtree
    for l in lines:
        if "$ cd /" in l:
            position=dirtree
        if "$ ls" in l:
            continue
        if "dir " in l:
            dirname=l.split(" ")[-1]
            dirs.append(position.add_child(dirname))
        
    input=lines[0]
    print(input)
    for i in range(3,len(input)):
        pack=set(input[i-13:i+1])
        if len(pack)==14:
            print(i+1)
            break
