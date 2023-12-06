cuboids = [s.replace('x=','').replace(',y=',' ').replace(',z=',' ').replace('..',' ') for s in open("input_day22.txt").readlines()]
cuboids = [s.replace('on','1').replace('off','0') for s in cuboids]
cuboids = [[int(x) for x in s.split()] for s in cuboids]
#cuboids = [c for c in cuboids if abs(c[1]) <= 50] # for part 1

# a cuboid is represented as [+1/-1,xmin,xmax,ymin,ymax,zmin,zmax]
# where +1 is 'added cuboid' and -1 is 'subtracted cuboid'

# return the cuboid at the intersection of cuboids s and t
# if cuboid t is added, the intersection is subtracted, and vice versa
def intersection(s,t):
    mm = [lambda a,b:-b,max,min,max,min,max,min]
    n = [mm[i](s[i],t[i]) for i in range(7)]
    return None if n[1] > n[2] or n[3] > n[4] or n[5] > n[6] else n

cores = []
i=0
for cuboid in cuboids[0:7]:
    toadd = [cuboid] if cuboid[0] == 1 else [] # add cuboid to core if 'on'
    for core in cores:
        inter = intersection(cuboid,core)
        if inter:
            toadd += [inter] # if nonempty, add to the core later
    cores += toadd
    if i==7:
        print(toadd)
    i+=1

def countoncubes(cores):
    oncount = 0
    for c in cores:
        oncount += c[0] * (c[2]-c[1]+1) * (c[4]-c[3]+1) * (c[6]-c[5]+1)
    return oncount

print('On cubes:', countoncubes(cores))