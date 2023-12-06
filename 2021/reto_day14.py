import time

#f = open("input_day14.txt", "r")
totalSteps=10
f = open("id14pru.txt", "r")
input=f.read()
lines=input.splitlines()
template=lines[0]
rules={}
for i in range(2,len(lines)):
    rules[lines[i].split(" -> ")[0]]=lines[i].split(" -> ")[1]

newTemplate=template
for i in range(totalSteps):
    print(i)
    pairs=[]
    start = time.time()
    for j in range(len(newTemplate)-1):
        pairs.append(newTemplate[j]+newTemplate[j+1])
    end = time.time()
    print("1. "+str(end-start))
    newPairs=[]
    start = time.time()
    for p in pairs:
        p2=p[0]+rules[p]
        newPairs.append(p2)
        lastLetter=p[1]
    end = time.time()
    print("2. "+str(end-start))
    
    newTemplate=''.join(newPairs)+lastLetter
    #print(newTemplate)
contador = {i:newTemplate.count(i) for i in newTemplate}
res=max(contador.values())-min(contador.values())
print(res)