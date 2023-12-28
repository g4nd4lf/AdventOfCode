import os
os.chdir("./day8")
print(os.getcwd())
#input1='sample2.txt'
input1='input.txt'

with open(input1) as f:
    lines=f.readlines()
    print(lines[0])
    commands=lines[0].replace('\n','')
    desertmap={}
    for l in lines[2:]:
      l=l.replace("\n","")
      src=l.split(" = ")[0]
      dst=l.split(" = ")[1]
      dst=tuple(dst[1:-1].split(', '))
      desertmap[src]=dst
    #print(desertmap)
    origins=[d for d in desertmap if d[-1]=='A']
    ends={}
    for i,o in enumerate(origins):
        ends[i]=-i-1
    #print(origins)
    pos=origins
    ic=0
    i=0
    fin=False
    pos6=pos[5]
    while not fin:
        #print(i,len(pos))
        c=commands[ic]
        if c=='L':
            pos6=desertmap[pos6][0]
            #pos=[desertmap[p][0] for p in pos]
        else:
            pos6=desertmap[pos6][1]
            #pos=[desertmap[p][1] for p in pos]
        i+=1
        ic+=1
        if ic==len(commands):
            ic=0
        #fin=True
        if pos6[-1]=='Z':
            print(i,ic)
        # for j,p in enumerate(pos):
        #     if p[-1]!='Z':
        #         fin=False
        #     else:
        #         if j==6:
        #             print(j,i,ic)
    print(i)


   