import heapq
import os
os.chdir("./day19")
#input1='sample.txt'
input1='input.txt'
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

with open(input1) as f:
    lines=f.readlines()
    blank_line_idx=lines.index("\n")
    workflows_lines=lines[:blank_line_idx]
    ratings_lines=lines[blank_line_idx+1:]
    workflows={}
    for i,l in enumerate(workflows_lines):
        key,values = l.split("{")
        values=values.replace("}","").replace("\n","")
        values=values.split(",")
        arr=[]
        for x in values[:-1]:
            arr.append(x.split(":"))
        arr.append(["True" , values[-1]])
        workflows[key]=arr
    ratings=[]
    for i,l in enumerate(ratings_lines):
        rating={}
        l=l.replace("{","").replace("}\n","").replace("}","")
        rating_list=l.split(",")
        for r in rating_list:
            key,value=r.split("=")
            rating[key]=value#int(value)
        ratings.append(rating)
result=0
for r in ratings:
    destination="in"
    #result=transite(result,workflows,r)
    #print(result)
    while destination not in ["A","R"]:
        destination=transite(destination,workflows,r)
    if destination=="A":
        result+=evaluate(r)
        print(r)
print("result: ",result)

#print("workflows: ",workflows)
#print("ratings",ratings)