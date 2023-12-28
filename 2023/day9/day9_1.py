import os
from operator import itemgetter

os.chdir("./day9")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'
def resta(arr):
    if len(arr)>2:
        return arr[0]-resta(arr[1:])
    else:
        return arr[0]-arr[1]

def dif(lista):
    derivada = [lista[i + 1] - lista[i] for i in range(len(lista) - 1)]
    return derivada

with open(input1) as f:
    lines=f.readlines()
    data=[]
    for l in lines:
      l=l.replace("\n","")
      dataline=[int(x) for x in l.split()]
      data.append(dataline)
    #print(data)
res=0
res2=0
for d in data:
    ddif=d
    last=[d[-1]]
    first=[d[0]]
    while any([x!=0 for x in ddif]):
        ddif=dif(ddif)
        last.append(ddif[-1])
        first.append(ddif[0])
        #print(ddif)
    #print(first)
    res+=sum(last)
    signo=1
    partial=0    
    for f in first:
        res2+=signo*f
        partial+=signo*f
        signo=-signo
        #res2+=resta(first)
    #print("partial:", partial)
print(res)
print(res2)
    