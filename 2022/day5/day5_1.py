import os

def move(stack,qt,fr,to):
    print(stack)
    new=stack[fr][0:qt]
    new.reverse()
    stack[fr]=stack[fr][qt:]
    stack[to]=new+stack[to]
    print(stack)
#input1='./day5/sample.txt'
input1='input.txt'
#input1 = 'sample.txt'
stacks=0
print(os.getcwd())
stack=[]
with open(input1) as f:
    #lines = f.readlines()
    lines = f.read().splitlines() 
    #GET NUMBER OF STACKS
    for l in lines:
        if "1" in l:
            #print(l.split(" ")[-2])
            stacks=int(l.split(" ")[-2])
            break
    #GET STARTING STACKS 
    for i in range(stacks):
        stack.append([])
    for l in lines:
        if "1" in l:
            break
        else:
            for i in range(stacks):
                if l[i*4+1]!=' ':
                    stack[i].append(l[i*4+1])
    #READ PROCEDURE
    for l in lines:
        step=l.split(' ')
        if step[0]=="move":
            qt=int(step[1])
            fr=int(step[3])-1
            to=int(step[5])-1
            move(stack,qt,fr,to)
print(''.join([x[0] for x in stack]))