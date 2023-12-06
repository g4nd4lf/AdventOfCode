#import pandas as pd
import os
os.chdir("./2023/day5")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'

def find_single_points(ranges):
    single_points=set()
    if ranges[0][0]>0:
        single_points.update([0,ranges[0][0]-1])
    for i,r in enumerate(ranges):
        single_points.update(r)
        if i<(len(ranges)-1):
            if ranges[i+1][0]-ranges[i][1]>1:
                single_points.update([r[1]+1,ranges[i+1][0]-1])
    return single_points

def map_point(origin, map):
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
   
seeds=[int(x) for x in seeds]
seed_rg=set()
for i in range(0,len(seeds),2):
    seed_rg.add((seeds[i],seeds[i]+seeds[i+1]))

def include(x,y):
    if x[0]<=y[0] and x[1]>=y[1]:
        return True
    else:
        return False
def dividir(input,map):
    res=set()
    nomaps=True
    for mi in map:
        m=(mi[1],mi[1]+mi[2]-1)
        if include(m,i):
            res.add(input)
            nomaps=False
        elif include(i,m):
            res.update(((i[0],m[0]-1),(m[0],m[1]),(m[1]+1,i[1])))
            nomaps=False
        elif i[0] <= m[0] <= i[1]:
            res.update(((i[0],m[0]-1),(m[0],i[1])))
            nomaps=False
        elif i[0] <= m[1] <= i[1]:
            res.update(((i[0],m[1]),(m[1]+1,i[1])))
            nomaps=False
    if nomaps:
        res.add(input)
    return res

def mapea(inputs,map):
    outputs=set()
    for i in inputs:
        outputs.add((map_point(i[0],map),map_point(i[1],map)))
    return outputs


input=seed_rg
for map in maps:
    newinputs=set()
    for i in input:
        div=dividir(i,map)
        for d in div:
            if d[0]==0:
                print("Encontrado 0!")
        if len(div)>0:
            newinputs.update(div)
        else:
            newinputs.add(div)
    newoutputs=mapea(newinputs,map)
    input=newoutputs

print(min([x[0] for x in newoutputs if x[0]!=0]))