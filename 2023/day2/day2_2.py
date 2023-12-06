#import pandas as pd
import os
os.chdir("./2023/day2")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'
#bag=[12,13,14] #red, green, blue 
with open(input1) as f:
    lines = f.readlines()
    result=0
    bags=[]
    for l in lines:
        bag=[0,0,0]
        game,rest=l.split(":")
        id=game.split(" ")[1]
        rounds=rest.split(";")
        valid_game=True
        for r in rounds:
            elements=r.split(' ')
            for i,item in enumerate(elements):
                if 'red' in item:
                    if int(elements[i-1])>bag[0]:
                        bag[0]=int(elements[i-1])
                if 'green' in item:
                    if int(elements[i-1])>bag[1]:
                        bag[1]=int(elements[i-1])
                if 'blue' in item:
                    if int(elements[i-1])>bag[2]:
                        bag[2]=int(elements[i-1])
        power=bag[0]*bag[1]*bag[2]
        result+=power
    print(result)