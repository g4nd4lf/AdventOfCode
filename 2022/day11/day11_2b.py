import os
import math
import numpy as np
import pathlib

currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)

inputFile='input.txt'
#inputFile='sample.txt'
x=[1]
cycles=0
#Read input
monkeys=[]
with open(inputFile) as f:
    lines = f.read().splitlines()
    for l in lines:
        if "Monkey" in l:
            monkeys.append({"items":[],"operation":"","test":0,"res":[],"inspections":0})
        if "Starting" in l:
            monkeys[-1]["items"]=l.split("items: ")[1].split(", ")
        if "Operation" in l:
            monkeys[-1]["operation"]=l.split("new = ")[1]
        if "Test" in l:
            monkeys[-1]["test"]=l.split("by ")[1]
        if "true" in l or "false" in l:
            monkeys[-1]["res"].append(int(l.split("monkey ")[1]))
lcm=1
for m in monkeys:
    lcm*=int(m["test"])
for rounds in range(10000):
    #print(rounds)#,len(monkeys))
    for m in monkeys:
        for i in range(len(m["items"])):
            m["inspections"]+=1
            old=int(m["items"].pop(0))
            new=eval(m["operation"])
            if new > lcm:
                remainder = new % lcm
                new = lcm + remainder
            #new=new//3
            if not bool(new%int(m["test"])):
                monkeys[m["res"][0]]["items"].append(new)
            else:
                monkeys[m["res"][1]]["items"].append(new)
    #print(monkeys)
insp=[x["inspections"] for x in monkeys]
print(insp)
insp.sort(reverse=True)
print((insp[0]*insp[1]))
