import os,math
from z3 import *

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
result=""
for i,t in enumerate(trayectories[:3]):
    vxsign = "+" if math.copysign(1, t[1][0])==1 else "-"
    vysign = "+" if math.copysign(1, t[1][1])==1 else "-"
    vzsign = "+" if math.copysign(1, t[1][2])==1 else "-"
    result+=f"(x0+t{i}*vx=={t[0][0]}{vxsign}t{i}*{abs(t[1][0])}) and "
    result+=f"(y0+t{i}*vy=={t[0][1]}{vxsign}t{i}*{abs(t[1][1])}) and "
    result+=f"(z0+t{i}*vz=={t[0][2]}{vzsign}t{i}*{abs(t[1][2])}) and "
result=result[:-5]
x0=Real('x0')
y0=Real('y0')
z0=Real('z0')

vx=Real('vx')
vy=Real('vy')
vz=Real('vz')

t0=Real('t0')
t1=Real('t1')
t2=Real('t2')
#sol=solve(parse_smt2_string(result))
sol=solve((x0+t0*vx==150191335679733+t0*239) and (y0+t0*vy==257950211885619+t0*57) and (z0+t0*vz==282767497332049+t0*42) and (x0+t1*vx==310843966440013-t1*42) and (y0+t1*vy==307550528062309-t1*26) and (z0+t1*vz==305058399233591-t1*8) and (x0+t2*vx==240206072440513+t2*44) and (y0+t2*vy==257955942583195+t2*13) and (z0+t2*vz==339853739319015+t2*18))
print("Result: ",result)
print("Solution: ",sol)

