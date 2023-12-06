#f = open("id17pru.txt", "r")
f = open("input_day17.txt", "r")
input=f.read()
line=input.splitlines()[0]
area=[]
xs=line.split("x=")[1].split(", y=")[0]
ys=line.split(", y=")[1]
area=[int(xs.split("..")[0]),int(xs.split("..")[1]),int(ys.split("..")[0]),int(ys.split("..")[1])]
print(area)

def trayectoria(vx,vy):
    xmin=area[0]
    xmax=area[1]
    ymin=area[2]
    ymax=area[3]
    x=vx
    y=vy
    if (xmin <= x <= xmax) and (ymin <= y <= ymax):
            return max(y,0)
    hmax=vy

    while True:
        vy-=1
        if vx>0:
            vx-=1
        elif vx<0:
            vx+=1
        else:
            vx=0
        x+=vx
        y+=vy
        if y>hmax:
            hmax=y
        #x=20..30, y=-10..-5
        if (xmin <= x <= xmax) and (ymin <= y <= ymax):
            return hmax
        if x>xmax or y<ymin:
            return -666
hmax=0
print(trayectoria(7,-1))

#print(trayectoria(6,3))
#print(trayectoria(6,9))

exitos=0
# for i in range(0,area[0]):
#     for j in range(0,-area[2]):
myRes=set()
for i in range(0,1000):
    for j in range(-200,200):
        h=trayectoria(i,j)
        if h>hmax:
            hmax=h
        if h!=-666:
            exitos+=1
            myRes.add((i,j))
            #print(str(i)+","+str(j))
print(hmax)
print(exitos)
print(".......")
f2 = open("id17pru_result.txt", "r")
input2=f2.read()
lines2=input2.splitlines()
res=set()
for l in lines2:
    for el in l.split():
        coor= el.split(",")
        res.add( (int(coor[0]),int(coor[1])) )
print(res)