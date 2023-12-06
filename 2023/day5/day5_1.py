#import pandas as pd
import os
os.chdir("./2023/day5")
print(os.getcwd())
input1='sample.txt'
#input1='input.txt'

def map(origin, map):
    origin=int(origin)
    for m in map:
        if origin in range(m[1],m[2]+m[1]):
            return m[0]+(origin-m[1])
    return origin


with open(input1) as f:
    text=f.read()
    seeds=text.split("seed-to-soil map:\n")[0].split("seeds: ")[1].split()
    rest=text.split("\n\n")[1:]
    maps=[]
    for r in rest:
        strings=r.split("\n")[1:]
        newmap=[]
        for s in strings:
            newmap.append([int(x) for x in s.split()])
        maps.append(newmap)
    print(maps)
locations=[]
for s in seeds:
    res=s
    for m in maps:
        s=map(s,m)
    locations.append(s)
print(locations,min(locations))