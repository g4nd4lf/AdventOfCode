import os,sys
import math
import numpy as np
import re
import time
from itertools import chain, combinations, permutations
import os,pathlib
from itertools import cycle

def calcula(name,monkeys):
    if isinstance(monkeys[name],int):
        return monkeys[name]
    else:
        num1=str(calcula(monkeys[name][0],monkeys))
        num2=str(calcula(monkeys[name][2],monkeys))
        return eval("".join([num1,monkeys[name][1],num2]))

#inputFile='input.txt'
inputFile='sample.txt'
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)

with open(inputFile) as f:
    print("leyendo fichero...")
    lines=f.read().splitlines()
monkeys={}
for l in lines:
    name=l.split(":")[0]
    yell=l.split(":")[1].strip()
    if yell.isdigit():
        monkeys[name]=int(yell)
    else:
        monkeys[name]=tuple(yell.split(" "))
print(calcula("root",monkeys)) 