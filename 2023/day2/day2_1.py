#import pandas as pd
import os
os.chdir("./2023/day2")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'
bag=[12,13,14] #red, green, blue 
with open(input1) as f:
    lines = f.readlines()
    result=0
    for l in lines:
        game,rest=l.split(":")
        id=game.split(" ")[1]
        rounds=rest.split(";")
        valid_game=True
        for r in rounds:
            elements=r.split(' ')
            for i,item in enumerate(elements):
                if 'red' in item:
                    if int(elements[i-1])>bag[0]:
                        valid_game=False
                if 'green' in item:
                    if int(elements[i-1])>bag[1]:
                        valid_game=False
                if 'blue' in item:
                    if int(elements[i-1])>bag[2]:
                        valid_game=False
        if valid_game:
            result+=int(id)
    print(result)