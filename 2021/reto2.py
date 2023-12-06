import pandas as pd
input=pd.read_csv("input2.txt",header=None)
input.columns=["data"]
def cuentaInc(df):
    df.columns=["data"]
    dif=df.diff()
    #dif=input.iloc[0:20].diff()
    print(len(dif.query('data>0')))

#Reto 1: Cuenta incrementos
cuentaInc(input)

#Reto 2: Sliding window

j=0
sum=[]
print(len(input))
for i in range(2,len(input)):
    sum.append(input.iloc[i]+input.iloc[i-1]+input.iloc[i-2])    
sumdf=pd.DataFrame(sum)
cuentaInc(sumdf)
i2=[199,200,208,210,200,207,240,269,260,263]
i2=pd.DataFrame(i2)
sum=[]
for i in range(2,len(i2)):
    sum.append(i2.iloc[i]+i2.iloc[i-1]+i2.iloc[i-2])    
sumdf2=pd.DataFrame(sum)
cuentaInc(sumdf2)

#Resultado:1316