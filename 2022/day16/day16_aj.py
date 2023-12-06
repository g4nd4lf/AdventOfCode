import sys, re, os
import pathlib
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)

#inputFile='input.txt'
inputFile='sample.txt'
#Read input
with open(inputFile) as f:
    print("leyendo fichero...")
    linesfile=f.readlines()
lines = [re.split('[\\s=;,]+', x) for x in linesfile]
G = {x[1]: set(x[10:]) for x in lines}
F = {x[1]: int(x[5]) for x in lines if int(x[5]) != 0}
I = {x: 1<<i for i, x in enumerate(F)}
T = {x: {y: 1 if y in G[x] else float('+inf') for y in G} for x in G}
for k in T:
    for i in T:
        for j in T:
            T[i][j] = min(T[i][j], T[i][k]+T[k][j])

def visit(v, budget, state, flow, answer):
    answer[state] = max(answer.get(state, 0), flow)
    for u in F:
        newbudget = budget - T[v][u] - 1
        if I[u] & state or newbudget <= 0: continue
        visit(u, newbudget, state | I[u], flow + newbudget * F[u], answer)
    return answer    

total1 = max(visit('AA', 30, 0, 0, {}).values())
visited2 = visit('AA', 26, 0, 0, {})
total2 = max(v1+v2 for k1, v1 in visited2.items() 
                   for k2, v2 in visited2.items() if not k1 & k2)
print(total1, total2)
maximus=0
finalk=[]
for k1, v1 in visited2.items():
    for k2, v2 in visited2.items():
        if not k1 & k2:
            ks=[k1,k2]
            suma=v1+v2
            if suma>maximus:
                finalk=ks
                maximus=suma
print("max: ",maximus)
print(finalk)

#1871 2416