#input1='sample.txt'
input1='input.txt'

with open(input1) as f:
    lines = f.readlines()

elves=[]
#elves[0]=[]
i=0
subtotal=0
for l in lines:
    if l!="\n":
        subtotal+=int(l)
    else:
        elves.append(subtotal)
        subtotal = 0
elves.append(subtotal)
print(max(elves))
elvesOrd=elves
elvesOrd.sort(reverse=True)
print(elvesOrd[0]+elvesOrd[1]+elvesOrd[2])
#elvesOrd=elves.sort(reverse=True)
#print(elves.sort(reverse=True)[0]+elves.sort(reverse=True)[1]+elves.sort(reverse=True)[2])