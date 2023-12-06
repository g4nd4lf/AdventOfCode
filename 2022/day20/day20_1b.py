import os,sys
import math
import numpy as np
import re
import time
from itertools import chain, combinations, permutations
import os,pathlib
from itertools import cycle

inputFile='input.txt'
#inputFile='sample.txt'
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)
#----------------------------------------------------------------
def mayor(r1,r2):
    return r1[0]>=r2[0] and r1[1]>=r2[1] and r1[2]>=r2[2] and r1[3]>=r2[3]

dec_key = 811589153
a1=[]
a2=[]
#sample=[0, -1, 0, 0, 0, 0, 0,0]
#sample=[0, 0, 0, 0, 0, 0, 1,0]
#sample=[6, -1, 2, 3, -2, 0, 4]
sample=[-7, -2, 2, 3, -1, 0, 4]

#end=len(sample)
def solve(task):
    rounds, mutliply = (1, 1) if task == 1 else (10, dec_key)
    with open("input.txt") as f:
        numbers = [int(n) * mutliply for n in f.readlines()]
    #numbers =[1, 2, -3, 3, -2, 0, 4]
    #numbers=[-166, 2, -3, 3, -257, 0, 4,7]
    numbers=sample
    mixed = [a for a in enumerate(numbers)]
    cyc = cycle(mixed.copy())
    zero_tuple = (numbers.index(0), 0)
    lm = len(mixed) - 1

    for _ in range(rounds * len(numbers)):
    #for _ in range(end):
        curr = next(cyc)
        idx_old = mixed.index(curr)
        mixed.remove(curr)
        idx_new = (idx_old + curr[1] + lm) % lm
        mixed.insert(idx_new, curr)
        a2.append([x[1] for x in mixed])

    idx_zero_tuple = mixed.index(zero_tuple)
    print("aj",sum([mixed[(idx_zero_tuple + i) % len(numbers)][1]
          for i in [1000, 2000, 3000]]))
    return(mixed,numbers)


#------MAIN----------------------------------------------------------
#print(arr0)
#arr=[1, 2, -3, 4, 0, 3, -2]


#arr0=[1, 12, -3, 3, -2, 0, 4]

with open(inputFile) as f:
    print("leyendo fichero...")
    lines=f.read().splitlines()
arr0=[int(x) for x in lines]
arr0=sample#[-166, 2, -3, 3, -257, 0, 4,7]

arr=arr0.copy()
for a in arr0:#[:end]:
    if a<0:
        arrInv=arr.copy()
        arrInv.reverse()
        idx=arrInv.index(a)
        arrInv.remove(a)
        #newidx=(idx-a+len(arr))%(len(arr))
        newidx=(len(arr0)-1+a+idx)%(len(arr0)-1)
        # if newidx==0 and idx-a != 0:
        #     arrInv=arrInv[:-1]+[a]+arrInv[-1]#[newidx]+[a]
        # else:
        arrInv=arrInv[:newidx]+[a]+arrInv[newidx:]
        arr=arrInv.copy()
        arr.reverse()
    else:
        idx=arr.index(a)
        arr.remove(a)
        newidx=(idx+a)%(len(arr0)-1)
        arr=arr[:newidx]+[a]+arr[newidx:]
    a1.append(arr.copy())
    #print(a,arr)

id=arr.index(0)
res=arr[(id+1000)%len(arr)]+arr[(id+2000)%len(arr)]+arr[(id+3000)%len(arr)]
mix,num=solve(task=1)
arr2=[x[1] for x in mix]
print(res)
print(arr2==arr) 
 #sol1:11037