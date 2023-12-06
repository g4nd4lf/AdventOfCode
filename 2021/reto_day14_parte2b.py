import time
from collections import defaultdict
import math
f = open("input_day14.txt", "r")
start = time.time()
totalSteps=40
#f = open("id14pru.txt", "r")
input=f.read()
lines=input.splitlines()
template=lines[0]
pairs={}
for j in range(len(template)-1):
    if (template[j]+template[j+1]) in pairs:
        pairs[template[j]+template[j+1]]+=1
    else:
        pairs[template[j]+template[j+1]]=1
rules={}
for i in range(2,len(lines)):
    rules[lines[i].split(" -> ")[0]]=[lines[i].split(" -> ")[0][0]+lines[i].split(" -> ")[1],lines[i].split(" -> ")[1]+lines[i].split(" -> ")[0][1]]
#newPairs = defaultdict(int)
antPairs=pairs.copy()

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
        newPair=rules[np]
        for n in newPair:
            if n in newPairs:
                newPairs[n]+=antPairs[np]
            else:
                newPairs[n]=antPairs[np]
        if(newPairs[np]>=antPairs[np]):
            newPairs[np]-=antPairs[np]
    antPairs2=antPairs.copy()
    antPairs=newPairs.copy()
    #print(newTemplate)
letters={}
for n in newPairs:
    if n[0] in letters:
        letters[n[0]]+=newPairs[n]
    else:
        letters[n[0]]=newPairs[n]
letters[template[-1]]+=1
l=list(letters.values())
l.sort()
res=l[-1]-l[0]
print("Solución: "+str(res))
end = time.time()
print(end-start)
print(newPairs)
print(letters)
