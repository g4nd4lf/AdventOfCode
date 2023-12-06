import os
import math
import numpy as np
import pathlib

currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)
#inputFile='input.txt'
inputFile='sample.txt'

def part1(cave):
    start = 0j
    end = complex(max(k.real for k in cave), max(k.imag for k in cave))
    min_dist = dijkstra(cave, start, end)
    print('Part 1:', min_dist)

x=[1]
cycles=0
#Read input
monkeys=[]
operations=[]
with open(inputFile) as f:
    lines = f.read().splitlines()
    i=0
    for l in lines:
        if "Monkey" in l:
            monkeys.append({"items":[],"operation":"","test":0,"res":[],"inspections":0})
            i+=1
        if "Starting" in l:
            monkeyItems=[int(i) for i in l.split("items: ")[1].split(", ")]
            [monkeys[-1]["items"].append(Item("item"+str(i),x,[])) for x in monkeyItems]
        if "Operation" in l:
            monkeys[-1]["operation"]=l.split("new = ")[1]
            operations.append(l.split("new = ")[1])
        if "Test" in l:
            monkeys[-1]["test"]=l.split("by ")[1]
        if "true" in l or "false" in l:
            monkeys[-1]["res"].append(int(l.split("monkey ")[1]))
#for m in monkeys:
#    for i in m["items"]:
#        i+=[0] *len(monkeys)    
for rounds in range(20):
    #print(rounds,len(monkeys[0]["items"]))
    for im in range(len(monkeys)):
        m=monkeys[im]
        for i in range(len(m["items"])):
            m["inspections"]+=1
            olditem=m["items"].pop(0)
            idx=operations.index(m["operation"])
            olditem.oper.append(idx)
            new=oper(olditem,operations)
            #new=newitem[0]
            #new=eval(m["operation"])
            #new=new//3
            if not bool(new%int(m["test"])):
                monkeys[m["res"][0]]["items"].append(olditem)
            else:
                monkeys[m["res"][1]]["items"].append(olditem)
    for im in range(len(monkeys)):
        m=monkeys[im]
        for i in m["items"]:
                if i[0]==74:
                    print(rounds,im,i)
        #print(monkeys)

insp=[x["inspections"] for x in monkeys]
print(insp)
insp.sort(reverse=True)
print((insp[0]*insp[1]))
