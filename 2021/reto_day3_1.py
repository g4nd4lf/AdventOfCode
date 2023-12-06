import pandas as pd
import numpy as np
#input=pd.read_csv("input_day3.txt",header=None)
#input.columns=["com","value"]
def elem(str,i):
    return str[i]
#Leemos los datos de entrada
f = open("input_day3.txt", "r")
input=f.read()
#Dividimos el string leido en un array de lineas
ilines=input.splitlines()
#Convertimos el array de lineas en un pandas (matriz)
df=pd.DataFrame(columns=range(0,len(ilines[0])))
for i in range(0,len(ilines)):
    df.loc[i]=list(ilines[i])
print(df)
#Con los siguiente sacamos la suma de cada columna:
def mascomun(df):
    sum=[0]*len(df.columns)
    sum=np.array(sum)
    for i in df.columns:
        sum[i]=df[i].astype(int).sum()
        print(sum[i])
    mascomun=(sum>len(df[0])/2).astype(int).astype(str)
    menoscomun=(sum<len(df[0])/2).astype(int).astype(str)
    return (mascomun,menoscomun)


#Si la suma es mayor que la mitad de la longitud de la columna
#significa que el 1 es más comun, sino lo contrario
    
def mascomun2(arr):
    sum=[0]*len(arr[0])
    sum=np.array(sum)
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            sum[j]=sum[j]+int(arr[i][j])
    gammaArr=(sum>len(ilines)/2).astype(int).astype(str)
    epsArr=(sum<len(ilines)/2).astype(int).astype(str)
    return (gammaArr,epsArr)

(gammaArr,epsArr)=mascomun(df)
df2=pd.DataFrame(ilines)
df2.columns=['data']
df1=df2[df2['data'].str.startswith('1')]

# for g in gammaArr:
#     if g=='1':
#         ilines.filter

gamma=int(''.join(gammaArr),2)
gammaS=bin(gamma)
eps=int(''.join(epsArr),2)
epsS=bin(eps)

print(gammaS)
#eps=~gamma
#epsS=bin(eps)
print(epsS)
#eps=(not(sum>len(ilines)/2)).astype(int)
#print(eps)
print(df1)
