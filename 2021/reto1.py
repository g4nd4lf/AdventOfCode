#Reto 1: Numero de incrementos
import pandas as pd
input=pd.read_csv("input.txt",header=None)

def cuentaInc(df):
    input.columns=["data"]
    dif=input.diff()
    #dif=input.iloc[0:20].diff()
    print(len(dif.query('data>0')))
cuentaInc(input)
#Resultado:1316