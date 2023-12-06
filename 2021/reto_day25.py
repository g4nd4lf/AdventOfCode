import re
import time
def imprime():
    newLines=[]
    for i in range(alto):
        newLine=[]
        for j in range(ancho):
            if (i,j) in left:
                newLine.append(">")
            elif (i,j) in down:
                newLine.append("v")
            else:
                newLine.append(".")
        print("".join(newLine))
        newLines.append(newLine)

#f = open("id25pru3.txt", "r")
f = open("input_day25.txt", "r")
input=f.read()
lines=input.splitlines()
ancho=len(lines[0])
alto=len(lines)
left=set()
down=set()
for i in range(alto):
    for j in range(ancho):
        c=lines[i][j]
        if c==">":
            left.add((i,j))
        elif c=="v":
            down.add((i,j))
step=0
fin=False
#imprime()
while not fin:
    fin=True
    le=left.copy()
    do=down.copy()
    for l in left:
        if l[1]==ancho-1:
            next=(l[0],0)
        else:
            next=(l[0],l[1]+1)
        #if lines[next[0]][next[1]]==".":
        if next not in left and next not in down:
            le.add(next)
            le.remove(l)
            fin=False
    left=le.copy()
    for d in down:
        if d[0]==alto-1:
            next=(0,d[1])
        else:
            next=(d[0]+1,d[1])
        if next not in left and next not in down:
            do.add(next)
            do.remove(d)
            fin=False
    down=do.copy()

    step+=1
    #print(str(step))
    #imprime()
print(str(step))
