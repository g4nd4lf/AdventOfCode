import os,sys
import math
import numpy as np
import pathlib
import re
import time
from itertools import chain, combinations, permutations

inputFile='input.txt'
#inputFile='sample.txt'
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)

#----------------------------------------------------------------
def mayor(r1,r2):
    return r1[0]>=r2[0] and r1[1]>=r2[1] and r1[2]>=r2[2] and r1[3]>=r2[3]

#------MAIN----------------------------------------------------------
#print(arr0)
#arr=[1, 2, -3, 4, 0, 3, -2]

#arr0=[1, -8, -3, 3, -2, 0, 4]
arr0=[1, 2, -3, -8, -2, 0, 4]

# with open(inputFile) as f:
#     print("leyendo fichero...")
#     lines=f.read().splitlines()
# arr0=[int(x) for x in lines]

arr=arr0.copy()
for a in arr0:
    idx=arr.index(a)
    arr.remove(a)
    
    #newidx=idx+a
    if a<0:
        arrInv=arr.copy()
        arrInv.reverse()
    else:
        newidx=(idx+a)%len(arr)
        arr=arr[:newidx]+[a]+arr[newidx:]
    print(a,arr)

id=arr.index(0)
res=arr[(id+1000)%len(arr)]+arr[(id+2000)%len(arr)]+arr[(id+3000)%len(arr)]
print(res)
 