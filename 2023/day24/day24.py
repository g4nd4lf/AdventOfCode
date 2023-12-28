import os

os.chdir("./day24")
#input1='sample.txt'
input1='input.txt'
xlim=[7,27]
ylim=[7,27]
xlim=[200000000000000,400000000000000]
ylim=xlim
def intersect(t1,t2):
    #x=-(b1-b2)/(a1-a2)  donde a=vy/vx   b=x0*vy/vx+y0/vy
    x0_1,y0_1,z0_1=t1[0]
    x0_2,y0_2,z0_2=t2[0]
    vx1,vy1,vz1=t1[1]
    vx2,vy2,vz2=t2[1]
    if vx1!=0 and vx2!=0 and vy1!=0 and vy2!=0:
        a1=vy1/vx1
        a2=vy2/vx2
        b1=-x0_1*vy1/vx1+y0_1
        b2=-x0_2*vy2/vx2+y0_2
        if (a1-a2)==0:
            return None,None
        else:
            x=-(b1-b2)/(a1-a2)
            y=a1*x+b1
            return x,y
    else:
        return None,None

print("Reading and parsing data:")
trayectories=[]
with open(input1) as f:
    lines=f.readlines()
    for j,l in enumerate(lines):
        l=l.replace("\n","")
        pos0,vel=l.split("@")
        pos0=[int(x) for x in pos0.split(",")]
        vel=[int(x) for x in vel.split(",")]
        trayectories.append([pos0,vel])
num_intersec=0
for i,t1 in enumerate(trayectories[:-1]):
    for t2 in trayectories[i+1:]: 
        x,y=intersect(t1,t2)
        if x==None:
            print(t1,t2,"paralelas")
        elif (t1[1][0]>0 and x<t1[0][0]) or (t2[1][0]>0 and x<t2[0][0]):     #vx>0 y x<x0 ->pasado
            print(t1,t2,"se cruzan en el pasado")
        elif (t1[1][0]<0 and x>t1[0][0]) or (t2[1][0]<0 and x>t2[0][0]):     #vx<0 y x>x0 ->pasado
            print(t1,t2,"se cruzan en el pasado")
        elif not (xlim[0]<=x<=xlim[1] and ylim[0]<=y<=ylim[1]):#x>xlimit -> out
            print(t1,t2,"se cruzan fuera del límite")
        else:
            print(t1,t2,"Se cruzan!")
            num_intersec+=1

print("Result: ",num_intersec)

