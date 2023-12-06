import time
import numpy as np
start = time.time()
f = open("id22pru2.txt", "r")
#f = open("input_day22.txt", "r")
input=f.read()
lines=input.splitlines()
# reactor=np.array([])
# for i in range(100):
#     r2d=np.array([])
#     for j in range(100):
#         r1d=np.array([0]*100)
#         r2d=np.append(r2d,r1d)
#     reactor=np.append(reactor,r2d)
reactor=np.zeros((101, 101, 101))
t1 = time.time()
print("Inicializado"+str(t1-start))
for line in lines[0:3]:
    mode=line.split(" ")[0]
    changesS=line.split(" ")[1].split(",")
    changes=[]
    for c in changesS:
        ini=int(c.split("..")[0][2:])+50
        fin=int(c.split("..")[1])+50
        #changes.append(ini)
        #changes.append(fin)
        rango=list(range(ini,fin+1))
        changesi=[]
        for r in rango:
            if 0<=r<=100:
                changesi.append(r)
        changes.append(changesi)

    #print(changes)
    for i in changes[0]:
        for j in changes[1]:
            for k in changes[2]:
                if mode=="on":
                    reactor[i][j][k]=1
                else:
                    reactor[i][j][k]=0
t2 = time.time()
print("Reactor modificado"+str(t2-start))
#unos = filter(lambda x: x==1, reactor)
print(np.sum(reactor))
t3 = time.time()
print("Suma realizada"+str(t3-start))
# for i in range(len(reactor)):
#     for j in range(len(reactor[0])):
#         for k in range(len(reactor[0][0])):
#             if reactor[i][j][k]==1:
#                 print(str(i),","+str(j)+","+str(k))
   