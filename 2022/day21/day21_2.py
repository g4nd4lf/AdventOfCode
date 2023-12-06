import os,sys
import math
import numpy as np
import re
import time
from itertools import chain, combinations, permutations
import os,pathlib
from itertools import cycle
def invOper(oper,n2,res,ord):
    if oper=="+":
        return(res-n2)
    elif oper=="-":
        if ord==1:
            return(n2-res)
        else:
            return(res+n2)
    elif oper=="*":
        return res/n2
    elif oper=="/":
        if ord==1:
            return n2/res
        else:
            return res*n2
def calcula(name,monkeys):
    if name=="humn" or name==None:
        return None
    if isinstance(monkeys[name],int):
        return monkeys[name]
    else:
        num1=str(calcula(monkeys[name][0],monkeys))
        num2=str(calcula(monkeys[name][2],monkeys))
        if num1=='None' or num2=='None':
            return None
        else:
            return eval("".join([num1,monkeys[name][1],num2]))
def estima(name,monkeys,number):
    name1=monkeys[name][0]
    oper=monkeys[name][1]
    name2=monkeys[name][2]
    if name1=="humn":
        n2=calcula(name2,monkeys)
        return invOper(oper,n2,number,2)
    elif name2=="humn":
        n2=calcula(name1,monkeys)
        return invOper(oper,n2,number,1)
    else:
        n1=calcula(name1,monkeys)
        if n1==None:
            n2=calcula(name2,monkeys)
            res=invOper(oper,n2,number,2)
            return estima(name1,monkeys,res)
        else:
            res=invOper(oper,n1,number,1)
            return estima(name2,monkeys,res)

    
inputFile='input.txt'
#inputFile='sample.txt'
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
name1=monkeys["root"][0]
name2=monkeys["root"][2]
res=calcula(name1,monkeys)
if res=='None' or res==None:
    number=calcula(name2,monkeys)
    humNumber=estima(name1,monkeys,number)
else:
    number=calcula(name1,monkeys)
    humNumber=estima(name2,monkeys,number)
print(humNumber) 