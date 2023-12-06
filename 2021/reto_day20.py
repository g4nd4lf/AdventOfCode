#f = open("id20pru.txt", "r")
f = open("input_day20.txt", "r")
input=f.read()
lines=input.splitlines()
algS=lines[0]
#alg0=[0 if x="." for x in alg]
#alg=list(map(lambda x:0 if x=="." else 1, algS))
print("alg:")
print(algS)
print(alg)
print("image:")
input=[]
inputS=[]

xlen=len(lines[2])
ylen=len(lines)-2
for i in range(ylen):
    inputS.append("".join(["."]*3*xlen))
for i in range(2,len(lines)):
    input.append(list(map(lambda x:0 if x=="." else 1, lines[i])))
    inputS.append("".join(["."]*xlen)+lines[i]+"".join(["."]*xlen))
    print(lines[i])
for i in range(ylen):
    inputS.append("".join(["."]*3*xlen))
print("inputS:")
for i in range(len(inputS)):
    print(inputS[i])
print("--------FIN1---------")
nxlen=len(inputS[0])
nylen=len(inputS)
myinputs=dict()

for i in range(nxlen):
    for j in range(nylen):
        myinputs[(i,j)]="."

#print(input)
for i in range(nylen):
    for j in range(nxlen):
        if i<ylen-1 or i>2*ylen+1 or j <xlen-1 or j>2*xlen+1:
            myinputs[(i,j)]="".join(["."]*9)
        else:
            myinputs[(i,j)]=""
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    myinputs[(i,j)]+=inputS[k][l]
            #print(myinputs[(i,j)])


def decode(input,alg):
    codeS="".join(list(map(lambda x:"0" if x=="." else "1", list(input))))
    code=int(codeS,2)
    return(algS[code])

out=decode(myinputs[(5,4)],alg)
print(out)

output=[]
for i in range(nylen):
    newLine=""
    for j in range(nxlen):
        out=decode(myinputs[(i,j)],alg)
        newLine+=out
    print(newLine)
    output.append(newLine)
print("-----------FIN2------------")
##########################
#Segunda aplicacion:
myinputs=dict()
inputS=output
ylen+=2
xlen+=2
for i in range(nylen):
    for j in range(nxlen):
        if i<int((nylen-ylen)/2)-1 or i>nylen-int((nylen-ylen)/2) or j <int((nxlen-xlen)/2)-1 or j>nxlen-int((nxlen-xlen)/2):
            myinputs[(i,j)]="".join(["."]*9)
        else:
            myinputs[(i,j)]=""
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    myinputs[(i,j)]+=inputS[k][l]
            #print(myinputs[(i,j)])

output=[]
for i in range(nylen):
    newLine=""
    for j in range(nxlen):
        out=decode(myinputs[(i,j)],alg)
        newLine+=out
    print(newLine)
    output.append(newLine)

total=0
for i in range(nylen):
    for j in range(nxlen):
        if output[i][j]=="#":
            total+=1
print("part1: "+str(total))