import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
import re
import ephem
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.dates as mdates
"""
Script para leer sensores Zim a partir de un archivo csv y representarlos
graficamente con interfaz interactiva que permita mostrar u ocultar cada sensor
INCLUYE sombreado para diferenciar dia y noche.
"""
graphsC1L = {}
graphsC2L = {}
graphsE1L = {}
graphsE2L = {}

def sunup(lat, long, time):
    """
    Dada latitud y longitud te dice si a una y fecha y hora indicada ha salido el sol o no
    """
    o = ephem.Observer()
    o.long = long
    o.lat = lat
    o.date = time
    s = ephem.Sun()
    s.compute(o)
    return s.alt > 0

def sombreaFechas(indices, ax, df):
    i = 0
    #while i < 10000:
    while i < len(indices)-1:
        ax.axvspan(df.index[indices[i]], df.index[indices[i] + 1], facecolor='grey', edgecolor='none', alpha=.5)
        i += 1
def sombreaFechas2(indices, ax, df):
    i = 0
    #while i < 10000:
    while i < len(indices)-1:
        #print(indices[i]+1)
        ax.axvspan(indices[i], indices[i+1], facecolor='wheat', edgecolor='none', alpha=.5)
        i += 1
def sombreaFechas3(anocheceres,amaneceres, ax,x):
    i = 0
    #while i < 10000:
    #x0=x[0]
    #xl=x[-1]
    if (anocheceres[0]>amaneceres[0]):
        anocheceres=anocheceres.insert(0,x[0])
    if (anocheceres[-1]>amaneceres[-1]):
        amaneceres=amaneceres.insert(len(x),x[-1])#.append(x[-1])
    
        #amaneceres.shift(freq=1)
        #amaneceres[0]=xmin
    while i < len(anocheceres):
        #print("de "+anocheceres[i])
        #print("a "+amaneceres[i])
        ax.axvspan(anocheceres[i], amaneceres[i], facecolor='wheat', edgecolor='none', alpha=.5)
        i += 1
def find_night_indices2(datetime_array):
    d2=datetime_array.to_series()
    d3=d2.apply(esnoche)
    return datetime_array[d3]

def find_night_indices(datetime_array):
    indices = []
    for i in range(len(datetime_array)):
        if not(sunup("37.25","-5.8",datetime_array[i])):
            indices.append(i)
    return indices
def esnoche(date):
    return not(sunup("37.25","-5.8",date))
def getTrat(label):
    #Usaremos este archivo para identificar los tratamientos asociados a cada sensor:
    zimResumen = pd.read_csv("../ResumenZims2019.csv", sep=';')
    parcela=re.search("P(.*)s",label).group(1)
    ch=label[-1]
    trat=zimResumen.query("Parcela=="+parcela+" & ch=="+ch)["Tratamiento"].values
    return trat
    
def on_pick(event):
    """
    Funcion para capturar el evento de pulsar en la leyenda y ocultar o mostrar esa grafica
    """
    legend = event.artist
    label=legend.get_label()
    trat=getTrat(label)
    #print(legend)
    isVisible = legend.get_visible()
    if trat=="C1L":
        graphsC1L[legend].set_visible(not isVisible)
    elif trat=="C2L":
        graphsC2L[legend].set_visible(not isVisible)
    elif trat=="E1L":
        graphsE1L[legend].set_visible(not isVisible)
    elif trat=="E2L":
        graphsE2L[legend].set_visible(not isVisible)
    
    legend.set_visible(not isVisible)
    fig.canvas.draw()
#Leemos en un dataframe los datos de los sensores Zim a partir de un csv:
zims=pd.read_csv("../allZims2019.csv")
zimArr=[]
myFmt = mdates.DateFormatter('%d/%m/%y\n%H:%M')
#Para graficar cada sensor con matplotlib necesitamos separarlos
# 1º convertimos el dataframe en un array. 
# Cada elemento del array representa un sensor, en forma de pareja de columnas (fecha, valor)
for col in range(1,len(zims.columns),2):
#for col in range(1,2,2):
#for col in range(7,len(zims.columns),2):
    #print(str(col)+": "+zims.columns[col])
    zimArr.append(zims.iloc[:,col:col+2])
#Creamos la figura que albergara las graficas:
#fig=plt.figure('Sondas Zim 2017')
#ax=fig.add_subplot(1,1,1)
for zim in zimArr:
    #La primera columna la convertimos de String a datetime
    zim.iloc[:,0]=pd.to_datetime(zim.iloc[:,0], infer_datetime_format=True)
    #Convertimos la primera columna en un indice
    zim=zim.set_index(zim.columns[0])
    #Añadimos el sensor convertido al array
    #dibujamos la linea correspondiente al sensor
    #print("columnas:")
    #print(zim.columns[0])
    #Se parte el array de datos en grupos de 15 dias
    zimArri = [g for n, g in zim.groupby(pd.Grouper(freq='16D'))]
    pp=PdfPages(zim.columns[0]+".pdf")
    fig=[]
    albas=[]
    auroras=[]
    j=0
    #for i in range(0,1,4):
    for i in range(0,len(zimArri),4):
        fig.append(plt.figure(j,figsize=(11.69,8.27)))
        fig[j].suptitle(zimArri[i].columns[0]+"_"+str(j), fontsize=16)
        ax=[]
        z=[]
        for k in range(0,min([4,len(zimArri)-i])):
            zi=zimArri[i+k]
            print("k: "+str(k))
            ax.append(fig[j].add_subplot(4,1,k+1))
            ax[k].tick_params(axis='both', which='major', labelsize=6)
            ax[k].xaxis.set_major_formatter(myFmt)
            ax[k].tick_params(axis="y",direction="in", pad=-10)
            ax[k].tick_params(axis="x",direction="in", pad=-5)
            znew,=ax[k].plot(zi.index,zi,label=zi.columns[0],linewidth=0.3)
            z.append(znew)
            d=zi.index.dropna().to_series().apply(esnoche)
            anochecer=d.loc[((d==True) & (d.shift()==False))]
            amanecer=d.loc[((d==False) & (d.shift()==True))]
            if(anochecer.index[0]==d.index[0]):
                anochecer=anochecer[1:]
            albas.append(anochecer)
            if(amanecer.index[0]==d.index[0]):
                amanecer=amanecer[1:]
            auroras.append(amanecer)
            sombreaFechas3(anochecer.index,amanecer.index, ax[k],zi.index)
        #night_indices1 = find_night_indices2(zimArri[i].index.dropna())
        #night_indices2 = find_night_indices2(zimArri[i+1].index.dropna())
        #night_indices3 = find_night_indices2(zimArri[i+2].index.dropna())
        #night_indices4 = find_night_indices2(zimArri[i+3].index.dropna())
        #sombreaFechas2(night_indices2, ax2, zimArri[i+1])
        #sombreaFechas2(night_indices3, ax3, zimArri[i+2])
        #sombreaFechas2(night_indices4, ax4, zimArri[i+3])
        pp.savefig(fig[j])
        j=j+1
    plt.show() 
    pp.close()
print("fin!")
    #z,=ax.plot(zim.index,zim,label=zim.columns[0])
    #night_indices = find_night_indices(zim.index.dropna())
    #sombreaFechas(night_indices, ax, zim)
#ax1=fig.add_subplot(4,1,1)
#sm4 = [g for n, g in zim.groupby(pd.Grouper(freq='15D'))]
#ax2=fig.add_subplot(4,1,2)
#ax3=fig.add_subplot(4,1,3)
#ax4=fig.add_subplot(4,1,4)
# #y dentro de la figura se crea un subplot:
# axC1L=fig.add_subplot(4,1,1)
# axC2L=fig.add_subplot(4,1,2)
# axE1L=fig.add_subplot(4,1,3)
# axE2L=fig.add_subplot(4,1,4)
# axC1L.title.set_text('C1L')
# axC2L.title.set_text('C2L')
# axE1L.title.set_text('E1L')
# axE2L.title.set_text('E2L')

# zArrC1L=[] #Array que albergará la referencia a cada linea 
# zArrC2L=[]
# zArrE1L=[]
# zArrE2L=[]
# #zArr=[]
# zimArr2=[] #Vamos a modificar cada pareja de columnas a una sola columna 
# #con los valores del sensor y convirtiendo la primera columna (convertida a tipo datetime) en indice
# #Hay que hacer todo esto para que se dibuje correctamente con matplotlib
# for zim in zimArr:
#     #La primera columna la convertimos de String a datetime
#     zim.iloc[:,0]=pd.to_datetime(zim.iloc[:,0], infer_datetime_format=True)
#     #Convertimos la primera columna en un indice
#     zim=zim.set_index(zim.columns[0])
#     #Añadimos el sensor convertido al array
#     zimArr2.append(zim)
#     #dibujamos la linea correspondiente al sensor
#     #print("columnas:")
#     #print(zim.columns[0])
#     trat=getTrat(zim.columns[0])
#     if trat=="C1L":
#         zC1L,=axC1L.plot(zim.index,zim,label=zim.columns[0])
#         zArrC1L.append(zC1L)
#         #zArr.append(zC1L)
#     elif trat=="C2L":
#         zC2L,=axC2L.plot(zim.index,zim,label=zim.columns[0])
#         zArrC2L.append(zC2L)
#         #zArr.append(zC2L)
#     elif trat=="E1L":
#         zE1L,=axE1L.plot(zim.index,zim,label=zim.columns[0])
#         zArrE1L.append(zE1L)
#         #zArr.append(zE1L)
#     elif trat=="E2L":
#         zE2L,=axE2L.plot(zim.index,zim,label=zim.columns[0])
#         zArrE2L.append(zE2L)
#         #zArr.append(zE2L)
#     #y la añadimos al array
     
# #Lo siguiente es necesario para crear una leyenda interactiva que permita
# #mostrar u ocultar cada linea al pulsar en su leyenda
# legendC1L = axC1L.legend(loc='upper right')
# legendC2L = axC2L.legend(loc='upper right')
# legendE1L = axE1L.legend(loc='upper right')
# legendE2L = axE2L.legend(loc='upper right')

# lgsC1L=legendC1L.get_lines()
# lgsC2L=legendC2L.get_lines()
# lgsE1L=legendE1L.get_lines()
# lgsE2L=legendE2L.get_lines()
# for lg in lgsC1L:
#     lg.set_picker(True)
#     lg.set_pickradius(10)
# for lg in lgsC2L:
#     lg.set_picker(True)
#     lg.set_pickradius(10)
# for lg in lgsE1L:
#     lg.set_picker(True)
#     lg.set_pickradius(10)
# for lg in lgsE2L:
#     lg.set_picker(True)
#     lg.set_pickradius(10)


# for i in range(0,len(lgsC1L)):
#     graphsC1L[lgsC1L[i]]=zArrC1L[i]
# for i in range(0,len(lgsC2L)):
#     graphsC2L[lgsC2L[i]]=zArrC2L[i]
# for i in range(0,len(lgsE1L)):
#     graphsE1L[lgsE1L[i]]=zArrE1L[i]
# for i in range(0,len(lgsE2L)):
#     graphsE2L[lgsE2L[i]]=zArrC2L[i]

# plt.connect('pick_event',on_pick)
#plt.show()