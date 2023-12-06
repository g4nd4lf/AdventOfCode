import os
import numpy as np

#inputFile='./day8/sample.txt'
#inputFile='input.txt'
inputFile='sample.txt'
with open(inputFile) as f:
    lines = f.read().splitlines()

edgeTreesNumber= 2*(len(lines)-1+len(lines[0])-1)
innerTrees = np.zeros( (len(lines)-2, len(lines[0])-2),dtype=int )
total= edgeTreesNumber
visibleInnerTrees =np.zeros( (len(lines)-2, len(lines[0])-2),dtype=int )
trees=[]
for i in range(len(lines)):
    newtrees=[]
    for j in range(len(lines[0])):
        newtrees.append(int(lines[i][j]))
    trees.append(newtrees)
npTrees=np.array(trees)
for i in range(len(innerTrees)):
    for j in range(len(innerTrees[0])):
        innerTrees[i,j] =lines[i+1][j+1]
        leftTrees=npTrees[i+1][0:j+1]
        if all(x <innerTrees[i,j] for x in leftTrees):
            visibleInnerTrees[i,j] = 1
        #visibleInnerTrees[i,j]=all(x <innerTrees[i,j] for x in leftTrees)
#right2left
for i in range(len(innerTrees)):
    for j in range(len(innerTrees[0])):
        rightTrees=npTrees[i+1][j+2:]
        upTrees=npTrees[0:i+1,j+1]
        downTrees=npTrees[i+2:,j+1]
        if (all(x <innerTrees[i,j] for x in rightTrees)) or (all(x <innerTrees[i,j] for x in upTrees)) or (all(x <innerTrees[i,j] for x in downTrees)) :
            visibleInnerTrees[i,j] = 1
        
#up2down
#for i in range(len(innerTrees)):
total=total+sum(sum(visibleInnerTrees))
print(total)