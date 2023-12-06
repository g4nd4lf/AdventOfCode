import pandas as pd
from collections import defaultdict
import numpy as np

combis=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
#signs=[(1,1),(-1,1),(1,-1),(-1,-1)]
sol=[[-892,524,684],[-876,649,763],[-838,591,734],[-789,900,-551],[-739,-1745,668],[-706,-3180,-659],[-697,-3072,-689],[-689,845,-530],[-687,-1600,576],[-661,-816,-575],[-654,-3158,-753],[-635,-1737,486],[-631,-672,1502],[-624,-1620,1868],[-620,-3212,371],[-618,-824,-621],[-612,-1695,1788],[-601,-1648,-643],[-584,868,-557],[-537,-823,-458],[-532,-1715,1894],[-518,-1681,-600],[-499,-1607,-770],[-485,-357,347],[-470,-3283,303],[-456,-621,1527],[-447,-329,318],[-430,-3130,366],[-413,-627,1469],[-345,-311,381],[-36,-1284,1171],[-27,-1108,-65],[7,-33,-71],[12,-2351,-103],[26,-1119,1091],[346,-2985,342],[366,-3059,397],[377,-2827,367],[390,-675,-793],[396,-1931,-563],[404,-588,-901],[408,-1815,803],[423,-701,434],[432,-2009,850],[443,580,662],[455,729,728],[456,-540,1869],[459,-707,401],[465,-695,1988],[474,580,667],[496,-1584,1900],[497,-1838,-617],[527,-524,1933],[528,-643,409],[534,-1912,768],[544,-627,-890],[553,345,-567],[564,392,-477],[568,-2007,-577],[605,-1665,1952],[612,-1593,1893],[630,319,-379],[686,-3108,-505],[776,-3184,-501],[846,-3110,-434],[1135,-1161,1235],[1243,-1093,1063],[1660,-552,429],[1693,-557,386],[1735,-437,1738],[1749,-1800,1813],[1772,-405,1572],[1776,-675,371],[1779,-442,1789],[1780,-1548,337],[1786,-1538,337],[1847,-1591,415],[1889,-1729,1762],[1994,-1805,1792]]
signs=[(1,1),(1,-1)]
s0  =[1 , 2, 3]
s1_0=[-1, 2,-3]
s4_1=[-3, 1,-2]
s4_0=[3,-1,-2]
totalBeacons=0
allBeacons=set()
solSet=set()
for i in range(len(sol)):
    n=tuple(sol[i])
    solSet.add(n)
#[88-68,113-1246,-1104-43]
def def_value():
    return 0


# for i in range(0,len(dfs)):
#     for j in range(0,len(dfs)):
#         if (i!=j):
#             (n,x1,x2)=coincidencias(dfs[i],dfs[j])

def difAbsolutasX(df1,df2):
    #Con esta funcion solo calculamos las diferencias de las coordenadas x de cada dataframe
    #difxs={(i,j):dif}
    difxs=defaultdict(def_value)
    for i in range(len(df1[0])):
        for j in range(len(df2[0])):
            difxs[(i,j)]=abs(abs(df1[0][i])-abs(df2[0][j]))
    return(difxs,1,2)

def difAbsolutas(df1,df2):
    #Con esta función calculamos diferencias de la coordenada x de df1 con las 3 coor de df2
    difs=[]
    for k in range(3):
        difxs=defaultdict(def_value)
        for i in range(len(df1[0])):
            for j in range(len(df2[k])):
                difxs[(i,j)]=abs(abs(df1[0][i])-abs(df2[k][j]))
        difs.append(difxs)
    return(difs)

def difAbsolutas(df1,df2):
    #Con esta función calculamos diferencias de la coordenada x de df1 con las 3 coor de df2
    difs=[]
    for k in range(3):
        difxs=defaultdict(def_value)
        for i in range(len(df1[0])):
            for j in range(len(df2[k])):
                difxs[(i,j)]=abs(abs(df1[0][i])-abs(df2[k][j]))
        difs.append(difxs)
    return(difs)

def diferencias(df1,df2):
    difs=[]
    for c in combis:
        for s in signs:
            difi=defaultdict(def_value)
            for i in range(len(df1[c[0]])):
                for j in range(len(df2[c[1]])):
                    difi[(c,s,i,j)]=s[0]*df1.loc[i,c[0]]-s[1]*df2.loc[j,c[1]]
            difs.append(difi)
    return difs

def cuentaRepeticiones(dicArr):
    maxRepsArr=[]
    diferenciaMasRepetidaArr=[]
    for j in range(len(dicArr)):
        arr=list(dicArr[j].values())
        my_dict = {i:arr.count(i) for i in arr}
        arr2=list(my_dict.values())
        arr2i=list(my_dict.keys())
        maxreps=max(arr2)
        id=arr2.index(maxreps)
        diferenciaMasRepetida=arr2i[id]
        maxRepsArr.append(maxreps)
        diferenciaMasRepetidaArr.append(diferenciaMasRepetida)
    return (maxRepsArr,diferenciaMasRepetidaArr)

def get_keys(val,dic):
    keys=[]
    for key, value in dic.items():
         if val == value:
             keys.append(key)
    return keys

def calculaCoorSat(df1,df2,beacons):
    coorSat=[0,0,0]
    for i in range(3):
        b=beacons[i][0]
        c1=b[0][0]
        s1=b[1][0]
        c2=b[0][1]
        s2=b[1][1]
        alpha=df1.loc[b[2],c1]
        beta=df2.loc[b[3],c2]
        coorSat[c1]=(s1*alpha-s2*beta)
    return(coorSat)

def reubica():
 pass
def reconfiguraSat(df,bs,coor):
    bs=[beacons[0][0][0:2],beacons[1][0][0:2],beacons[2][0][0:2]]
    axis=[bs[0][0][1],bs[1][0][1],bs[2][0][1]]
    newSigns=[bs[0][1][1],bs[1][1][1],bs[2][1][1]]
    print(axis)
    for i in range(len(df)):
        aux=list(df.loc[i,:]).copy()
        for j in range(3):
            b=bs[j]
            df.loc[i,j]=coor[j]+newSigns[j]*aux[axis[j]]
    return df

#f = open("id19pru.txt", "r")
f = open("input_day19.txt", "r")
input=f.read()
lines=input.splitlines()
line=lines[0]
satelites=[]
sat=[]
i=0
for l in lines:
    print(l)
    if l[0:3]!="---" and l!="":
        beaconStr=l.split(",")
        beacon=[int(x) for x in beaconStr]
        sat.append(beacon)
    if l=="" or i==len(lines)-1:
        satelites.append(sat)
        sat=[]
    i+=1
numSats=len(satelites)
print("Datos leidos.")
# for j in range(0,numSats):
#     sat=[]
#     i+=1
#     while i<len(lines):
#         if(lines[i]!=""):
#             break
#         beaconStr=lines[i].split(",")
#         print(lines[i])
#         beacon=[int(x) for x in beaconStr]
#         sat.append(beacon)
#         i+=1
#     i+=1
#     satelites.append(sat)

dfs=[]
dfsL=dict()
for j in range(0,numSats):
    df=pd.DataFrame(satelites[j])
    dfs.append(df)
dfsL[0]=dfs[0]
coincidencias=set()
coors=dict()
satelitesLocalizados=set()
satelitesLocalizados.add(0)
while len(satelitesLocalizados)<numSats:
    for i in range(len(dfs)):
        for j in range(len(dfs)):
            print("Recorrido: "+str(i)+","+str(j))
            print(satelitesLocalizados)
            if i!=j and i in satelitesLocalizados and j not in satelitesLocalizados:
                difs=diferencias(dfs[i],dfs[j])
                (numeroRepeticionesArr,diferenciaMasRepetidaArr)=cuentaRepeticiones(difs)
                if max(numeroRepeticionesArr)>11:
                    beacons=[]
                    for k in range(len(numeroRepeticionesArr)):
                        if (numeroRepeticionesArr[k]>11):
                            beaconsi=get_keys(diferenciaMasRepetidaArr[k],difs[k])
                            beacons.append(beaconsi)
                    newSigns= [ beacons[0][1][1][1],beacons[1][1][1][1],beacons[2][1][1][1] ]
                    coorSat=calculaCoorSat(dfs[i],dfs[j],beacons)
                    coincidencias.add((i,j))
                    coors[(i,j)]=coorSat
                    if i in satelitesLocalizados and j not in satelitesLocalizados:
                        dfnew=reconfiguraSat(dfs[j],newSigns,coorSat)
                        dfsL[j]=dfnew
                        satelitesLocalizados.add(j)
                        break
            if len(satelitesLocalizados)==numSats:
                break

allBeacons2=set()
for i in range(len(dfsL)):
    for j in range(len(dfsL[i])):
        newBeacon=tuple(dfsL[i].loc[j,:])
        allBeacons2.add(newBeacon)
print("part1:"+str(len(allBeacons2)))


a = np.array((1, 2, 3))
b = np.array((4, 5, 6))

dist = np.sqrt(np.sum(np.square(a-b)))

maxDistance=0
print(dist)
# for b1 in allBeacons2:
#     for b2 in allBeacons2:
#         if b1!=b2:
#             manhattanDistance=abs(b2[0]-b1[0])+abs(b2[1]-b1[1])+abs(b2[2]-b1[2])
#             if manhattanDistance>maxDistance:
#                 maxDistance=manhattanDistance

maxDistance=0
arrCoor=list(coors.values())
for a1 in arrCoor:
    for a2 in arrCoor:
        if a1!=a2:
            manhattanDistance=abs(a2[0]-a1[0])+abs(a2[1]-a1[1])+abs(a2[2]-a1[2])
            if manhattanDistance>maxDistance:
                maxDistance=manhattanDistance


print("part2: "+str(maxDistance))