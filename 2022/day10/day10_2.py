import os
import math
import numpy as np
import pathlib

currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)

inputFile='input.txt'
#inputFile='sample.txt'
x=[1,1]
cycles=1
#sprite=np.array([0,1,2])
sprite=[0,1,2]
screen=[]
spriteArr=[]
with open(inputFile) as f:
    lines = f.read().splitlines()
    for l in lines:
        newCommand=l.split(" ")
        #if cycles==218:
        #    print(cycles)
        if len(newCommand)>1:
            valStr=newCommand[1]
            val=int(valStr)
            if (cycles-1)%40 in sprite:
                screen.append(1)
            else:
                screen.append(0)
            spriteArr.append(sprite.copy())
            x.append(x[cycles])
            cycles+=1
            if (cycles-1)%40 in sprite:
                screen.append(1)
            else:
                screen.append(0)
            spriteArr.append(sprite.copy())
            x.append(x[cycles]+val)
            sprite=[x[cycles+1]-1,x[cycles+1],x[cycles+1]+1]
            #sprite+=x[cycles+1]
            cycles+=1
        else:
            if (cycles-1)%40 in sprite:
                screen.append(1)
            else:
                screen.append(0)
            spriteArr.append(sprite.copy())
            x.append(x[cycles])
            cycles+=1
            
sum=0
#for i in range(19,220,40):
#    sum+=(i+1)*x[i]
#    print(i+1,x[i],(i+1)*x[i])
   # print(len(points))    
#print(sum)
s=""
for i in range(len(screen)):
    if screen[i]:
        s+="#"
    else:
        s+="."
news="".join(s[i:i+40] + "\n" for i in range(0,len(s),40))
print(news)
#for i in range(1,21):
#    print(i,sprite,)