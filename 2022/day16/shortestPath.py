
import os,sys
import math
import numpy as np
import pathlib
import re

#inputFile='input.txt'
inputFile='sample.txt'
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)

#Read input
with open(inputFile) as f:
    print("leyendo fichero...")
    lines=f.readlines()
    valve={}
    for l in lines:
        #Valve OJ has flow rate=0; tunnels lead to valves EW, IG
        name=l[6:8]
        flow = re.search('has flow rate=(.*); tunnel', l).group(1)
        neigS=re.search('lead[s]? to valve[s]? (.*)',l).group(1)
        neig=neigS.split(", ")
        #valve["name"]=name
        valve[name]={"estado":0,"flow":int(flow),"neig":set(neig)}
        #print(valve,result.group(1),neig.group(1))
    #allopen=''.join([str(int(valve[x]["flow"]!=0)) for x in valve])

# graph = {'1': set(['2', '3']),
#          '2': set(['1', '5']),
#          '3': set(['1', '4']),
#          '4': set(['3','5']),
#          '5': set(['2', '4'])}

graph=valve

def bfs(graph, S, D):
    queue = [(S, [S])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex]["neig"] - set(path):
            if next == D:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

print(list(bfs(graph, 'AA', 'FF')))
def shortest(graph, S, D):
    try:
        return next(bfs(graph, S, D))
    except StopIteration:
        return None

print(shortest(graph, 'AA', 'FF'))