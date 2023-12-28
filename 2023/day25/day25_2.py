import os
from itertools import combinations
from collections import deque
import copy
import networkx as nx


os.chdir("./day25")
#input1='sample.txt'
input1='input.txt'


print("Reading and parsing data:")
g=nx.Graph()
with open(input1) as f:
    lines=f.readlines()
    for j,l in enumerate(lines):
        l=l.replace("\n","")
        orig=l.split(": ")[0]
        dest=l.split(": ")[1].split(" ")
        for d in dest:
            g.add_edge(orig,d)

cv,p=nx.stoer_wagner(g)
print("Result: ",len(p[0])*len(p[1]))

