import re
import time
#f = open("id24pru3.txt", "r")
f = open("input_day24.txt", "r")
input=f.read()
lines=input.splitlines()
params=[]
tramas=[]
for i in range(14):
    tramas.append(lines[18*i:18*i+18])
    if tramas[i][4]=="div z 1":
        params.append(int(tramas[i][15].split(" ")[2])) 
    else:
        params.append(int(tramas[i][5].split(" ")[2]))
w=[9]*14
#w5<7 (cond 7)
#w4<7 (cond 8)
#w1<3 (cond 13)
w[5]=6
w[4]=7
w[1]=2
n=params

while True:
    fin=True
    w[3]=w[2]+n[2]+n[3]
    w[6]=w[5]+n[5]+n[6]
    w[7]=w[4]+n[4]+n[7]
    w[9]=w[8]+n[8]+n[9]
    w[11]=w[10]+n[10]+n[11]
    w[12]=w[1]+n[1]+n[12]
    w[13]=w[0]+n[0]+n[13]
    for i in range(14):
        if w[i]>9 or w[i]<1:
            fin=False
    if fin:
        break
    else:
        if w[10]>1:
            w[10]-=1
        elif w[8]>1:
            w[8]-=1
        elif w[5]>1:
            w[5]-=1
        elif w[4]>1:
            w[4]-=1
        elif w[2]>1:
            w[2]-=1
        elif w[1]>1:
            w[1]-=1
        elif w[0]>1:
            w[0]-=1
            for i in [10,8,2]:
                w[i]=9
            w[5]=6
            w[4]=6
            w[1]=2
            w[10]>1

        print(w)
#parte2:
#cond 4: w2>3
#cond 10: w8>5
#cond 14: w0>8
#cond 12: w10>1
w2=[1]*14
w2[2]=4
w2[8]=6
w2[0]=9
w2[10]=2
w2[3]=w2[2]+n[2]+n[3]
w2[6]=w2[5]+n[5]+n[6]
w2[7]=w2[4]+n[4]+n[7]
w2[9]=w2[8]+n[8]+n[9]
w2[11]=w2[10]+n[10]+n[11]
w2[12]=w2[1]+n[1]+n[12]
w2[13]=w2[0]+n[0]+n[13]
code="".join([str(x) for x in w])
print(code)
code2="".join([str(x) for x in w2])
print(code2)

#92967699949891
#9141114361 1081
#9141114361 2181
#0123456789