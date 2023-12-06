import os

#input1='./day2/sample.txt'
input1='input.txt'

win={'A Y','B Z','C X'}
draw={'A X','B Y','C Z'}
total=0
print(os.getcwd())
with open(input1) as f:
    #lines = f.readlines()
    lines = f.read().splitlines() 
    for l in lines:
        if l in win:
            total+=6
        elif l in draw:
            total+=3
        if l[-1]=='X':
            total+=1
        elif l[-1]=='Y':
            total+=2
        else:
            total+=3
        print(total)
print(total)