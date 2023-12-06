import time
from collections import defaultdict
import math
#f = open("input_day14.txt", "r")
start = time.time()
totalSteps=20
f = open("id14pru.txt", "r")
input=f.read()
lines=input.splitlines()
template=lines[0]
pairs={}
for j in range(len(template)-1):
    pairs[template[j]+template[j+1]]=1
rules={}
for i in range(2,len(lines)):
    rules[lines[i].split(" -> ")[0]]=[lines[i].split(" -> ")[0][0]+lines[i].split(" -> ")[1],lines[i].split(" -> ")[1]+lines[i].split(" -> ")[0][1]]
#newPairs = defaultdict(int)
antPairs={}
for p in pairs:
    antPairs[p]=1
for i in range(totalSteps):
    if i==totalSteps-1:
        s1=time.time()
    print(i)
    if i==totalSteps-1:
        e0=time.time()
    newPairs=antPairs.copy()
    if i==totalSteps-1:
        e1=time.time()
    for np in antPairs:
        e2=time.time()
        for j in range(antPairs[np]):
            if i==totalSteps-1:
               e3=time.time()
            newPair=rules[np]
            for n in newPair:
                if n in newPairs:
                    newPairs[n]+=1
                else:
                    newPairs[n]=1
            if(newPairs[np]>0):
                newPairs[np]-=1
            if i==totalSteps-1:
                e4=time.time()
            if i==55:
                print("s1-e1,s1-e2,s1-e3,e4-e3")
                print(e1-s1)
                print(e2-s1)
                print(e3-s1)
                print(e4-s1)
                print(e4-e3)
    antPairs2=antPairs.copy()
    antPairs=newPairs.copy()
    #print(newTemplate)
letters={}
for n in newPairs:
    if n[0] in letters:
        letters[n[0]]+=newPairs[n]
    else:
        letters[n[0]]=newPairs[n]
    if n[1] in letters:
        letters[n[1]]+=newPairs[n]
    else:
        letters[n[1]]=newPairs[n]
for l in letters:
    letters[l]=math.ceil(letters[l]/2)
l=list(letters.values())
l.sort()
res=l[-1]-l[0]
print("Solución: "+str(res))
end = time.time()
print(end-start)
print("s1,e1,e2,e3,e4")
print(s1)
print(e1)
print(e2)
print(e3)
print(e4)
print("s1-e1,s1-e2,s1-e3,e4-e3")
print(s1-e1)
print(s1-e2)
print(s1-e3)
print(s1-e4)
print(e4-e3)

#print(letters)
#print(newPairs)
