import os

#input1='./day4/sample.txt'
input1='input.txt'
#input1 = 'sample.txt'
total=0
print(os.getcwd())
with open(input1) as f:
    #lines = f.readlines()
    lines = f.read().splitlines() 
    for l in lines:
        elf1=[int(x) for x in l.split(',')[0].split('-')]
        elf2=[int(x) for x in l.split(',')[1].split('-')]
        if elf1[0]>=elf2[0] and elf1[1] <= elf2[1]:
            total+=1
        elif elf2[0]>=elf1[0] and elf2[1] <= elf1[1]:
            total+=1
        
        # elf1set=set(range(elf1[0],elf1[1]+1))
        # elf2set=set(range(elf2[0],elf2[1]+1))
        
        # print(total)
print(total)