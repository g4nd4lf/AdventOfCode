import re, math

def numAnidamientos(ini,lista):
    res=0
    for i in range(0,ini):
        if lista[i]=="[":
            res+=1
        elif lista[i]=="]":
            res-=1
    return res
def sustituye(new,id,lista):
    nuevaLista=lista[:id[0]]+new+lista[id[1]:]
    return nuevaLista
def splitea(id,lista):
    num=int(lista[id[0]:id[1]])
    n1=math.floor(num/2)
    n2=math.ceil(num/2)
    nuevaLista=sustituye("["+str(n1)+","+str(n2)+"]",id,lista)
    #cambio=len("["+str(n1)+","+str(n2)+"]")-len(str(num))
    return nuevaLista
def addList(lista,nuevaLista):
    res="["+lista+","+nuevaLista+"]"
    return res
def parValue(id,lista):
    nums=lista[id[0]+1:id[1]-1].split(",")
    n1=int(nums[0])
    n2=int(nums[1])
    val=3*n1+2*n2
    return(val)
def magnitud(lista):
    res=0
    newLine=lista
    while True:
        #buscamos los pares en line:
        pares=re.findall(r'\[\d+,\d+\]',newLine)
        #print(pares)
        #Buscamos sus indices de inicio y fin:
        pares2=re.finditer(r'\[\d+,\d+\]',newLine)
        indices=[(m.start(0), m.end(0)) for m in pares2]
        #print(indices)
        if indices:
            res=parValue(indices[0],newLine)
            newLine=sustituye(str(res),indices[0],newLine)
            # cambio=0
            # for id in indices:
            #     i2=id[0]+cambio
            #     f2=id[1]+cambio
            #     res=parValue((i2,f2),newLine)
            #     newLine=sustituye(str(res),(i2,f2),newLine)
            #     cambio=f2-i2-len(str(res))
        else:
            return(res)
            break

def explode(id,lista):
    ini=id[0]
    fin=id[1]
    par=lista[ini+1:fin-1]
    #print("par: "+par)
    n1=int(par.split(",")[0])
    n2=int(par.split(",")[1])
    nl=lista
    numsALaIzquierda=re.findall(r'\d+',lista[0:ini])
    if len(numsALaIzquierda)>0:
        numeroALaIzquierda=numsALaIzquierda[-1]
        numsIter=re.finditer(r'\d+',lista[0:ini])
        ids=[(m.start(0), m.end(0)) for m in numsIter]
        nuevoNumero=n1+int(numeroALaIzquierda)
        nl=sustituye(str(nuevoNumero),ids[-1],lista)
        cambio=(len(str(nuevoNumero))-len(numeroALaIzquierda))
        ini+=cambio
        fin+=cambio        
    #     print("numero a la izquierda: "+numeroALaIzquierda)
    # else:
    #     print("Sin numeros a la izquierda")
    
    numsALaDcha=re.findall(r'\d+',nl[fin:])
    if len(numsALaDcha)>0:
        numALaDcha=numsALaDcha[0]
        numsIter=re.finditer(r'\d+',nl[fin:])
        idp=[(m.start(0), m.end(0)) for m in numsIter][0]
        idg=[x+fin for x in idp]
        nuevoNumero=n2+int(numALaDcha)
        nl=sustituye(str(nuevoNumero),idg,nl)
        #print("numero a la derecha: "+numALaDcha)
    #else:
        #print("Sin numeros a la derecha")
    
    nl=sustituye("0",(ini,fin),nl)
    #print(nl)
    return nl

def reduce(line):
    newLine=line
    iter=0
    while True:
        #buscamos los pares en line:
        pares=re.findall(r'\[\d+,\d+\]',newLine)
        #print(pares)
        #Buscamos sus indices de inicio y fin:
        pares2=re.finditer(r'\[\d+,\d+\]',newLine)
        indices=[(m.start(0), m.end(0)) for m in pares2]
        paresPorExplotar=[]
        for i in indices:
            i1=i[0]
            if (numAnidamientos(i1,newLine))>=4:
                paresPorExplotar.append(i)
        #print(indices)
        if paresPorExplotar:
            i1=paresPorExplotar[0][0]
            f1=paresPorExplotar[0][1]  
            #print(numAnidamientos(id[0],newLine))
            if (numAnidamientos(i1,newLine))>=4:
                #print("explode: "+str(id))
                newLine=explode((i1,f1),newLine)
                #fin=False
                continue
        #buscamos los numeros mayores de 9:
        #Buscamos los indices de inicio y fin de cada digito:
        digitos=re.finditer(r'\d+',newLine)
        indices=[(m.start(0), m.end(0)) for m in digitos]
        numerosPorExplitar=[]
        for i in indices:
            i1=i[0]
            f1=i[1]    
            digito=newLine[i1:f1]
            if int(digito)>9:
                numerosPorExplitar.append(i)    
        if numerosPorExplitar:
            i1=numerosPorExplitar[0][0]
            f1=numerosPorExplitar[0][1]    
            digito=newLine[i1:f1]
            if int(digito)>9:
                newLine=splitea(numerosPorExplitar[0],newLine)
                #print(newLine)
                #fin=False
                continue
        iter+=1
        if (not paresPorExplotar and not numerosPorExplitar):
            break
    return newLine

#f = open("id18pru4.txt", "r")
f = open("input_day18.txt", "r")
input=f.read()
lines=input.splitlines()
newLine=lines[0]
print(newLine)
for i in range(1,len(lines)):
#for i in range(1,2):
    if i==6:
        print("Linea 6")
        print(lines[i])
    #print("l["+str(i)+"]: "+lines[i])
    suma=addList(newLine,lines[i])
    #print("suma["+str(i)+"]: "+suma)
    newLine=reduce(suma)
    #print("sumaRed["+str(i)+"]: "+newLine)
    #print()

print("parte1: "+str(magnitud(newLine)))


#PART2:
maxMag=0
for i in range(len(lines)):
    sum1=lines[i]
    for j in range(len(lines)):
        if j!=i:
            sum2=lines[j]
            suma=reduce(addList(sum1,sum2))            
            mag=magnitud(suma)
            #print("mag: "+str(mag))
            if mag>maxMag:
                maxMag=mag
                print(lines[i])
                print(str(i)+"+"+str(j))
                print(lines[j])
                print("max: "+str(maxMag))
                


#Magnitudes:
# f2 = open("id18pru5.txt", "r")
# input=f2.read()
# lines=input.splitlines()
# for l in lines:
#     print(l,end=": ")
#     print(str(magnitud(l)))
