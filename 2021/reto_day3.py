import pandas as pd
import numpy as np
#input=pd.read_csv("input_day3.txt",header=None)
#input.columns=["com","value"]
def elem(str,i):
    return str[i]
#Leemos los datos de entrada
f = open("input_day3.txt", "r")
#f = open("id3pru.txt", "r")
input=f.read()
#Dividimos el string leido en un array de lineas
ilines=input.splitlines()
#Convertimos el array de lineas en un pandas (matriz)
df=pd.DataFrame(columns=range(0,len(ilines[0])))
for i in range(0,len(ilines)):
    df.loc[i]=list(ilines[i])
#print(df)
#Con los siguiente sacamos la suma de cada columna:
def mascomun(df):
    suma=[0]*len(df.columns)
    suma=np.array(suma)
    for i in df.columns:
        print(i)
        suma[i-df.columns[0]]=df[i].astype(int).sum()
        print(suma[i-df.columns[0]])
    print(suma)
    masComun=(suma>len(df[i])/2).astype(int).astype(str)
    menosComun=(suma<len(df[i])/2).astype(int).astype(str)
    igualComun=(suma==len(df[i])/2).astype(int).astype(str)
    return (masComun,menosComun,igualComun)
(masComun, menosComun,igualComun)=mascomun(df)
#print(df[df[0]==masComun[0]])
print("0:")
print(igualComun)
df0=df
df2=df
for i in range(0,len(df.columns)):
    a0=str(int(masComun[0])or(int(igualComun[0])))
    #print("a0: "+str(a0))
    df=df[df.iloc[:,0]==a0].iloc[:,1:]   
    #print("columna["+str(i)+"]:")
    #print(len(df))
    if (len(df)>1):
        (masComun, menosComun,igualComun)=mascomun(df)
        print(str(i))
        print(masComun)
        print(igualComun)
    else:
        resO=df0.loc[df.index]
        #print("resultado:")
        #print(res)
        break
print("CALCULOS CO2:")
(masComun, menosComun,igualComun)=mascomun(df0)
for i in range(0,len(df2.columns)):
    #b0=str(int(menosComun[0])or(int(igualComun[0])))
    b0=str(int(menosComun[0]))#or(int(igualComun[0])))
    #print("a0: "+str(a0))
    df2=df2[df2.iloc[:,0]==b0].iloc[:,1:]
    print(i)
    print(df2)   
    #print("columna["+str(i)+"]:")
    #print(len(df))
    if (len(df2)>1):
        (masComun, menosComun,igualComun)=mascomun(df2)
        # print(str(i))
        # print(menosComun)
        # print(igualComun)
    else:
        resCO2=df0.loc[df2.index]
        #print("resultado:")
        #print(res)
        break
print("FIN")
#Si la suma es mayor que la mitad de la longitud de la columna
#significa que el 1 es más comun, sino lo contrario
def df2str(df):
    dfS=df.astype(str)
    res=""
    for i in dfS.columns:
        res+=(dfS[i])
    return res
res2O=df2str(resO)
res2CO2=df2str(resCO2)
oxig=int(res2O.values[0],2)
CO2sc=int(res2CO2.values[0],2)
print("oxigen:")
print(oxig)
print("CO2:")
print(CO2sc)
print("producto: ")
print(oxig*CO2sc)
def mascomun2(arr):
    sum=[0]*len(arr[0])
    sum=np.array(sum)
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            sum[j]=sum[j]+int(arr[i][j])
    gammaArr=(sum>len(ilines)/2).astype(int).astype(str)
    epsArr=(sum<len(ilines)/2).astype(int).astype(str)
    return (gammaArr,epsArr)

# (gammaArr,epsArr)=mascomun(df)
# df2=pd.DataFrame(ilines)
# df2.columns=['data']
# df1=df2[df2['data'].str.startswith('1')]

# # for g in gammaArr:
# #     if g=='1':
# #         ilines.filter

# gamma=int(''.join(gammaArr),2)
# gammaS=bin(gamma)
# eps=int(''.join(epsArr),2)
# epsS=bin(eps)

# print(gammaS)
# #eps=~gamma
# #epsS=bin(eps)
# print(epsS)
# #eps=(not(sum>len(ilines)/2)).astype(int)
# #print(eps)
# print(df1)
