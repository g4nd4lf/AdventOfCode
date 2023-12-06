import os,sys
import math
import numpy as np
import pathlib
maxx=4000000
#maxx=20
maxy=maxx

inputFile='input.txt'
#inputFile='sample.txt'

def contorno(s,d):
    i1=s[0]-d-1
    i2=s[0]+d+1
    #j1=s[1]-d-1    
    #j2=min(maxy,s[1]+d+1)
    vecinos=set()
    for i in range(i1,i2+1):
        j1=p[0][1]-(d-abs(i-p[0][0]))-1
        j2=p[0][1]+(d-abs(i-p[0][0]))+1
        if i>=0 and i<=maxx and j1>=0 and j2<=maxy:
            vecinos.update([(i,j1),((i,j2))])
    return vecinos
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)
def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

pairs=set()
beacons=set()
sensors=set()
imposible=set()
imposible2=set()
#Read input
with open(inputFile) as f:
    print("leyendo fichero...")
    lines=f.readlines()
    for l in lines:
        sensor=(int(l.split(": closest beacon is at ")[0].split("Sensor at x=")[1].split(", y=")[1]),int(l.split(": closest beacon is at ")[0].split("Sensor at x=")[1].split(", y=")[0]))
        beacon=(int(l.split(": closest beacon is at x=")[1].split(", y=")[1]),int(l.split(": closest beacon is at x=")[1].split(", y=")[0]))
        sensors.add(sensor)
        beacons.add(beacon)
        d=dist(sensor,beacon)
        pairs.add((sensor,beacon,d))
    print("recorriendo pares...")
    # k=0
    # for i in range(maxx):
    #     imp=[]
    #     for p in pairs:
    #         di=max(0,d-abs(i-p[0][0]))
    #         if len(imp)==0:
    #             imp=(p[0][1]-di,p[0][1]+di)
    #         else:

    #     for j in range(maxy):
    #         if j==maxy-1:
    #             print(i)
    #         for p in pairs:
    #             if (i,j)==p:
    #                 print(i,j) 
    # imp=[]
    # n=0
    for p in pairs:
        d=dist(p[0],p[1])
        vecinos=contorno(p[0],d)
        for v in vecinos:
            libre=True
            for p2 in pairs:
                d2=dist(p2[0],p2[1])
                if dist(v,p2[0])<=d2:
                    libre=False
            if libre:
                print("Encontrado:",v)
                print("solucion p2:",v[1]*4000000+v[0])
                quit()

    #     d=dist(p[0],p[1])
    #     i1=max(0,p[0][0]-d)
    #     i2=min(maxx,p[0][0]+d)
    #     j1=max(0,p[0][1]-d)
    #     #j1=p[0][1]-d
    #     j2=min(maxy,p[0][1]+d)        
    #     imp[n]=((i1,i2),(j1,j2))

         
    #     print(k,"/",len(pairs))
    #     k+=1
        
    #     #i1=max(0,p[0][0]-d)
    #     i1=max(0,p[0][0]-d)
    #     i2=min(maxx,p[0][0]+d)
    #     j1=max(0,p[0][1]-d)
    #     #j1=p[0][1]-d
    #     j2=min(maxy,p[0][1]+d)
    #     for i in range(i1,i2):
    #     #for i in range(20):
    #     #for i in [2000000]:
    #         j1=p[0][1]-(d-abs(i-p[0][0]))
    #         j2=p[0][1]+(d-abs(i-p[0][0]))
    #         # if i not in imposible:
    #         #     imposible[i]=(j1,j2)
    #         # else:
    #         #     add
    #         # y=list(range(j1,j2))
    #         # y=list(range(p[0][1]-(i1-i),p[0][1]+(i2-i)+1))
    #         # for j in y:
    #         #     imposible.add((i,j))
    #         #[imposible.add((i,x)) for x in y]
    #         for j in range(j1,j2+1):
    #             if dist((i,j),p[0])<=d and (i,j) not in beacons:
    #                imposible.add((i,j))
        
    # sum=0
    # print("calculando suma...")
    # for i in imposible:
    #     if i[0]==2000000:
    #         sum+=1
    # print(sum)
    # for i in range(maxx):
    #     for j in range(maxy):
    #         if (i,j) not in imposible and (i,j) not in sensors and (i,j) not in beacons:
    #             print("encontrado: ",i,j)
    # for i in range(20):
    #         linea=""
    #         for j in range(20):
    #             if (i,j) in imposible:
    #                 linea+="#"
    #             elif (i,j) not in sensors and (i,j) not in beacons:
    #                 linea+="."
    #                 print("Encontrado: ",i,j)
    #             if (i,j) in sensors:
    #                 linea+="S"
    #             if (i,j) in beacons:
    #                 linea+="B"
                    
                # if (i,j) not in imposible and (i,j) not in beacons:
                #     print("Encontrado: ",i,j)
            #print(linea)
    #for i in range(-2,22):
    #    for j in range(-2,25):
    #print("part1:",sandsResting)

    # for m in map:
    #     if 
    # for path in paths:
    #     for i in range(len(path)-1):
    #         if path[i][0]==path[i+1][0]:
    #             #print("")
    #             pass