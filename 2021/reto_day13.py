import pandas as pd
def pmu(x):
    if x>1:
        print(x)

def resetUnos(x):
    if x>=2:
        return 1
    else:
        return x
def doblaX(matrix,l):
    subMat1=matrix.iloc[:,0:l]
    subMat2=matrix.iloc[:,l+1:]
    subMat2 = subMat2.T.reset_index(drop=True).T
    subMat2i=pd.DataFrame(columns=subMat1.columns)
    for i in range(len(subMat2.columns)):
    #for i in range(len(subMat2)-1,-1,-1):
        subMat2i[i]=subMat2[len(subMat2.columns)-1-i]
    
    suma=subMat1.add(subMat2i,fill_value=0).astype(int)
    suma=suma.applymap(resetUnos)

    # for i in range(len(suma)):
    #     for j in range(len(suma.columns)):
    #         if suma.iloc[i][j]>1:
    #             suma.loc[i,j]=1
    return suma
def doblaY(matrix,l):
    subMat1=matrix.iloc[0:l,:]
    subMat2=matrix.iloc[l+1:,:]
    subMat2.reset_index(drop=True, inplace=True)
    subMat2i=pd.DataFrame(columns=subMat1.columns)
    for i in range(len(subMat2)):
    #for i in range(len(subMat2)-1,-1,-1):
        subMat2i.loc[i]=subMat2.loc[len(subMat2)-1-i]
    
    suma=subMat1.add(subMat2i,fill_value=0).astype(int)
    suma=suma.applymap(resetUnos)

    return suma
def leeDatos(file):
    f = open(file, "r")
    input=f.read()
    ilinesS=input.split("\n")
    mat=[]
    for i in range(len(ilinesS)):
        linea=[]
        for j in range(len(ilinesS[0])):
            linea.append(ilinesS[i][j])
        mat.append(linea)
    return(mat)


def cuentaPuntos(matrix):
    sumaPuntos=0
    for i in range(len(matrix)):
        for j in range(len(matrix.columns)):
            if matrix.loc[i,j]>0:
                sumaPuntos+=1
    return sumaPuntos
#f = open("id13pru.txt", "r")
f = open("input_day13.txt", "r")
input=f.read()
xpapel=[]
ypapel=[]
instrucciones=[]
ilinesS=input.splitlines()
i=0
modoInstrucciones=False
while (i<len(ilinesS)):
    if ilinesS[i]=="":
        modoInstrucciones=True
    else:
        if modoInstrucciones:
            instrucciones.append(ilinesS[i])
        else:
            ilines=[int(x) for x in ilinesS[i].split(",")]
            xpapel.append(ilines[0])
            ypapel.append(ilines[1])
    i+=1
xlen=max(xpapel)+1
ylen=max(ypapel)+3
papel = pd.DataFrame(0, index=range(ylen), columns=range(xlen))
for i in range(len(xpapel)):
    papel[xpapel[i]][ypapel[i]]=1
#print(papel)
newPapel=papel
k=0
print("Tamaño original: "+str(len(newPapel))+", "+str(len(newPapel.columns)))
for ins in instrucciones:
    if ins.split("=")[0]=="fold along y":
        newPapel=doblaY(newPapel,int(ins.split("=")[1]))
    else:
        newPapel=doblaX(newPapel,int(ins.split("=")[1]))
    print("puntos["+str(k)+"]: ",end="")
    print(newPapel.sum().sum(),end=" ")
    print("Tamaño: "+str(len(newPapel))+", "+str(len(newPapel.columns)))
    k+=1
#print(newPapel)
print("PUNTOS FINALES:")
print(newPapel.sum().sum())
#print(newPapel)
letras=[]
n2=newPapel.astype(str)
for p in n2.index:
    p2=n2.loc[p].str.cat()
    p3=p2.replace("0", ".")
    p4=p3.replace("1", "#")
    print(p4)

paper0=pd.DataFrame(leeDatos("paper0.txt"))
