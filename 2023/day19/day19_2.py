import heapq
import os
os.chdir("./day19")
#input1='sample.txt'
input1='input.txt'
def findCombinations(conditions):
    #conditions=['m>2090', 'a>=2006', 's<1351']
    pieces=['x','m','a','s']
    valids={}
    for p in pieces:
        bt=[0]
        lt=[4001]
        bte=[1]
        lte=[4000]  
        for c in conditions:
            if p+">=" in c:
                bte.append(int(c.split(">=")[1]))
            elif p+"<=" in c:
                lte.append(int(c.split("<=")[1]))
            elif p+">" in c:
                bt.append(int(c.split(">")[1]))
            elif p+"<" in c:
                lt.append(int(c.split("<")[1]))
        pmax=min(min(lte),min(lt)-1)
        pmin=max(max(bte),max(bt)+1)
        valids[p]=pmax-pmin+1
    if any(p in valids for p in pieces):
        combinations=1
    else:
        combinations=0
    for p in valids:
        combinations*=valids[p]
    return combinations
            
def findOrigin(workflows,destination):
    origins=[]
    for w in workflows:
        for i,x in enumerate(workflows[w]):
            if x[1]==destination:
                return i,w
        #arr=[(i,x) for i,x in enumerate(workflows[w]) if x[1]==destination]
        #origins.append(arr)
    #return origins
def findAllConditions(workflows,name,idx):
    conditions=[]
    conditions+=findMyConditions(workflows[name],idx)
    destination=name
    while destination !='in':
        i,destination = findOrigin(workflows,destination)
        conditions+=findMyConditions(workflows[destination],i)
    return conditions

def findMyConditions(workflow,idx):
    conditions=[workflow[idx][0]]
    #negConditions=[]
    for i in range(idx):
        if "<" in workflow[i][0]:
            newcondition=workflow[i][0].replace("<",">=")
        else:
            newcondition=workflow[i][0].replace(">","<=")
        conditions.append(newcondition)
    
    return conditions

def evaluate(rating):
    res=0
    for r in rating:
        res+=int(rating[r])
    return res
def transite(destination,workflows,r):
    workflow=workflows[destination]
    for w in workflow:
        if w[0]=='True':
            return w[1]
        else:
            vble=w[0][0]
            oper=w[0][1]
            num=w[0][2:]
            if eval(r[vble]+oper+num):
                return w[1]
            else:
                continue
    #return workflow

print("Reading and parsing data:")
workflows={}   
with open(input1) as f:
    data=f.read()
with open(input1) as f:
    lines=f.readlines()
    blank_line_idx=lines.index("\n")
    workflows_lines=lines[:blank_line_idx]
    for i,l in enumerate(workflows_lines):
        key,values = l.split("{")
        values=values.replace("}","").replace("\n","")
        values=values.split(",")
        arr=[]
        for x in values[:-1]:
            arr.append(x.split(":"))
        arr.append(["True" , values[-1]])
        workflows[key]=arr
    rs=0
    aes=0
combinations=0
for w in workflows:
#    if len(w)>2:
#        print(w,data.count(w))
        arr=[(i,x) for i,x in enumerate(workflows[w]) if x[1]=='A']
        narr=len(arr)
        if narr>0:
            for r in arr:
                conditions=findAllConditions(workflows,w,r[0])
                newCombination=findCombinations(conditions)
                combinations+=newCombination
                print(w,r,conditions,newCombination)
                pass

print("FINAL RESULT: ", combinations)
#         break
# #print("r: ",rs, " a: ",aes)