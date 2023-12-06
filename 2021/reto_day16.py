import binascii
from anytree import Node, RenderTree, PreOrderIter, findall_by_attr, Walker

# assert part_2(sample_data[4]) == 3
# assert part_2(sample_data[5]) == 54
# assert part_2(sample_data[6]) == 7
# assert part_2(sample_data[7]) == 9
# assert part_2(sample_data[8]) == 1
# assert part_2(sample_data[9]) == 0
# assert part_2(sample_data[10]) == 0
# assert part_2(sample_data[11]) == 1    
numLine=0
#f = open("id16pru4.txt", "r")
f = open("input_day16.txt", "r")
totalV=0
packs=[]
def opera(operacion, nodos):
    op=operacion
    if op==0:#suma
        res=0
        for ch in nodos:
            res=res+ch.name[0]        
    elif op==1:
        res=1
        for ch in nodos:
            res=res*ch.name[0]
    elif op==2:
        res=1e9
        for ch in nodos:
            if(ch.name[0])<res:
                res=ch.name[0]
    elif op==3:
        res=0
        for ch in nodos:
            if(ch.name[0])>res:
                res=ch.name[0]
    elif op==3:
        res=0
        for ch in nodos:
            if(ch.name[0])>res:
                res=ch.name[0]
    elif op==5:
        res=(nodos[0].name[0]>nodos[1].name[0])
    elif op==6:
        res=(nodos[0].name[0]<nodos[1].name[0])
    elif op==7:
        res=(nodos[0].name[0]==nodos[1].name[0])
    return res
def calcula(arbol):
    global hojasRecorridas
    operandosOk=True
    for d in arbol.children:
        operandosOk=True
        if d not in hojasRecorridas:
            if d.name[2]!=4: # no es literal
                res=calcula(d)
                operandosOk=False
    if operandosOk: #tengo todos los operandos
        res=opera(arbol.name[2],arbol.children)
        arbol.name[0]=res
        hojasRecorridas.add(arbol)
        return res
    else:
        calcula(arbol)
    #return res

def leeLiteral(parent,packetV,ms):
    numberB=""
    for i in range(0,len(ms),5):
        numberB+=ms[i+1:i+5]
        if(ms[i]=='0'):
            packs.append(Node([int(numberB,2),packetV,4],parent))
            return (numberB,ms[i+5:])

def leePack(parent,ms):
    global totalV
    packetVb=ms[0:3]
    typeIDb=ms[3:6]
    packetV=int(packetVb,2)
    totalV+=packetV
    typeID=int(typeIDb,2)
    if typeID==4:#literal
        (num,nms)=leeLiteral(parent,packetV,ms[6:])        
        print("literal: "+str(int(num,2)))
        vsum=0
    else:
        (vsum,nms)=leeOperator(parent,packetV,typeID,ms[6:])
    return(vsum,nms)

def leeOperator(parent,packetV,typeID,ms):
    lengthID=ms[0]
    packs.append(Node([0,packetV,typeID],parent))
    if lengthID=="0":
        totalLength=int(ms[1:16],2)
        print("totalLength: "+str(totalLength))
        (vsum,ms)=leeSubPacketsByLength(packs[-1],ms[16:],totalLength)
    else:
        numberOfPackets=int(ms[1:12],2)
        print("numberOfPackets: "+str(numberOfPackets))
        (vsum,ms)=leeSubPacketsByNumber(packs[-1],ms[12:],numberOfPackets)
    return (vsum,ms)


def leeSubPacketsByLength(parent,ms,length):
    vsum=0
    nextms=ms
    while True:
        (vsumi,newms)=leePack(parent,nextms)
        vsum+=vsumi
        if (len(ms)-len(newms))>=length:
            return (vsum,newms)
        else:
            nextms=newms

def leeSubPacketsByNumber(parent,ms,number):
    vsum=0
    nextms=ms
    for i in range(number):   
        (vsumi,newms)=leePack(parent,nextms)
        vsum+=vsumi
        nextms=newms
    return (vsum,newms)


input=f.read()
lines=input.splitlines()
line=lines[numLine]
num_of_bits=4
msg0=bin(int(line,16))[2:].zfill(num_of_bits)
leadingZeros=""
for i in range(0,4):
    if msg0[i]=="0":
        leadingZeros+="0"
    else:
        break
#leadingZeros+="0"
print(msg0)
msg=bin(int(line,16))[2:].zfill(len(line)*4) #mensaje recibido pasado a binario
#msg=leadingZeros+msg
print(line)
print(msg)
packetVb=msg[0:3]
typeIDb=msg[3:6]
packetV=int(packetVb,2)
totalV+=packetV
typeID=int(typeIDb,2)
#fullcode.name=[0,packetV,typeID]
fullcode=Node([0,packetV,typeID])
if typeID==4:
    (num,ms)=leeLiteral(fullcode,packetV,typeID,msg[6:])
    print("number: "+num+" "+str(int(num,2)))
else:
    (vsum,ms)=leeOperator(fullcode,packetV,typeID,msg[6:])
    print("operador: "+ms)
print("part1: "+str(totalV))
hojasRecorridas=set()
res=calcula(fullcode.children[0])
for pre, fill, node in RenderTree(fullcode.children[0]):
        print("%s%s" % (pre, node.name))
print(fullcode.children[0].name[0])

# while len(fullcode.leaves):
#     for hoja in fullcode.leaves:
#         if hoja not in hojasRecorridas:
#             papi=hoja.parent                            
#             op=papi.name[2]
#             if op==0:#suma
#                 res=0
#                 for ch in nodos:
#                     res=res+ch.name[0]
#                 print(papi)
#                 print(res)
#             elif op==1:
#                 res=1
#                 for ch in nodos:
#                     res=res*ch.name[0]
#                 print(papi)
#                 print(res)
#             elif op==2:
#                 res=1e9
#                 for ch in nodos:
#                     if(ch.name[0])<res:
#                         res=ch.name[0]
#                 print(papi)
#                 print(res)
#             elif op==3:
#                 res=0
#                 for ch in nodos:
#                     if(ch.name[0])>res:
#                         res=ch.name[0]
#                 print(papi)
#                 print(res)
#             elif op==3:
#                 res=0
#                 for ch in nodos:
#                     if(ch.name[0])>res:
#                         res=ch.name[0]
#                 print(papi)
#                 print(res)
#             elif op==5:
#                 res=(nodos[0].name[0]>nodos[1].name[0])
#                 print(papi)
#                 print(res)
#             elif op==6:
#                 res=(nodos[0].name[0]<nodos[1].name[0])
#                 print(papi)
#                 print(res)
#             elif op==7:
#                 res=(nodos[0].name[0]==nodos[1].name[0])
#                 print(papi)
#                 print(res)
#             papi.name[0]=res
#             print("TOTAL: "+str(res))
#             for ch in nodos:
#                 hojasRecorridas.add(ch)            
#                 ch.parent=None