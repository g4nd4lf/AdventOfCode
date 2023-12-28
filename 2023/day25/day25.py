import os
from itertools import combinations
from collections import deque
import copy

os.chdir("./day25")
#input1='sample.txt'
input1='input.txt'
def numgroups(elements,dlinks,ilinks):
    def getelements(elem,dlinks,ilinks):
        cola=deque()
        cola.append(elem)
        visited=set()
        while len(cola)>0:
            e=cola.popleft()
            if e in visited:
                continue
            visited.add(e)
            if e in dlinks:
                elems=dlinks[e]
                cola.extend(elems)
                pass
            if e in ilinks:
                elems=ilinks[e]
                cola.extend(elems)
                pass
        return visited

    group=set()
    el=list(elements)[0]
    els=getelements(el,dlinks,ilinks)
    group.update(els)
    if group==elements:
        return 1
    else:
        firstGroup=len(group)
        for e in elements:
            if e not in group:
                group.update(getelements(e,dlinks,ilinks))
                if group==elements:
                    secondGroup=len(elements)-firstGroup
                    print("RESULT: ",firstGroup*secondGroup)
                    return 2
                else:
                    return 3
def obtener_combinaciones2(n):
    numeros = list(range(n + 1))
    combinaciones = list(combinations(numeros, 3))
    return combinaciones

def obtener_combinaciones(n):
    numeros = list(range(n + 1))
    for combinacion in combinations(numeros, 3):
        yield combinacion

print("Reading and parsing data:")
directlinks={}
invlinks={}
elements=set()
with open(input1) as f:
    lines=f.readlines()
    for j,l in enumerate(lines):
        l=l.replace("\n","")
        orig=l.split(": ")[0]
        dest=l.split(": ")[1].split(" ")
        elements.add(orig)
        for d in dest:
            elements.add(d)
            directlinks[orig]=dest
            if d not in invlinks:
                invlinks[d]=[orig]
            else:
                invlinks[d].append(orig)
    #for l in links:
ngroups=numgroups(elements,directlinks,invlinks)
print("Numero de grupos orginales: ",ngroups)
# Ejemplo de uso
alldests=directlinks.values()
numdests=sum(len(x) for x in alldests)
posiblecuts = obtener_combinaciones(numdests)
arrlinks=list(directlinks)
for i,p in enumerate(posiblecuts):
    if i%100==0:
        print(i)
    dlinks=copy.deepcopy(directlinks)
    ilinks={}
    id=0
    ncuts=0
    result=set()
    for i,a in enumerate(arrlinks):
        for e in directlinks[a]:
            if id in p:
                dlinks[a].remove(e)
                result.add(a+"/"+e)
                ncuts+=1
            if ncuts==3:
                break
            id+=1
        if ncuts==3:
            break
    for orig in dlinks:
        for d in dlinks[orig]:
            if d not in ilinks:
                ilinks[d]=[orig]
            else:
                ilinks[d].append(orig)
    ngroups=numgroups(elements,dlinks,ilinks)
    if ngroups==2:
        print("Result: ",result) 
#print("Result: ",num_intersec)

