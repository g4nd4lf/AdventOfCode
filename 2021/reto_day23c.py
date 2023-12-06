
hallway=[0,1,2,3,4,5,6,7,8,9,10]
roomA=[11,12]
roomB=[21,22]
roomC=[31,32]
roomD=[41,42]

#movimientos posibles:
11->0,1,3,5,7,



f = open("id11pru.txt", "r")
#f = open("input_day11.txt", "r")
def adyacentes(matrix,x,y):
    res=[]
    if (y-1)>0 :
        res.append([x,y-1])
        if (x-1)>=0 :
            res.append([x-1,y-1])
        if (x+1)<len(matrix) :
            res.append([x+1,y-1])
    if (x-1)>=0 :
        res.append([x-1,y])
        if (y+1)<len(matrix[0]) :
            res.append([x-1,y+1])
            res.append([x,y+1])
            if (x+1)<len(matrix[0]):
                res.append([x+1,y+1])
    return res

input=f.read()
ilinesS=input.splitlines()
ilines=[]
for i in range(0,len(ilinesS)):
    iline=[]
    for j in range(0,len(ilinesS[0])):
        iline.append(int(ilinesS[i][j]))
    ilines.append(iline)  
totalFlashes=0      
for d in range(2):
    #1. incrementamos 1 a todos
    for i in range(0,len(ilines)):
        for j in range(0,len(ilines[0])):
            ilines[i][j]+=1
    #2. buscamos 9s:
    flashes=[]
    for i in range(0,len(ilines)):
        for j in range(0,len(ilines[0])):
            if ilines[i][j]>9:
                flashes.append([i,j])
                totalFlashes+=1
    while (True):
        if len(flashes)<=0:
            #Hemos terminado eldia
            break
        else:
            for f in flashes:   
                ilines[f[0]][f[1]]=0
                arr=adyacentes(ilines,i,j)
                for el in arr:
                    if el not in f:
                        ilines[el[0]][el[1]]+=1
            flashes=[]
            for i in range(0,len(ilines)):
                for j in range(0,len(ilines[0])):
                    if ilines[i][j]>9:
                        flashes.append([i,j])
                        totalFlashes+=1
    for i in range(0,len(ilines)):
        for j in range(0,len(ilines[0])):
            print(str(ilines[i][j]),end='')
        print('')            
    print(" Total flashes: ",end="")
    print(totalFlashes)

#1. incrementar +1 a todos
#2. Buscar 9s, si no hay pasamos al día siguiente
#       si hay->para cada uno (flash): buscar los adyacentes y sumarle 1
#       Buscar 9s otra vez, si no hay (o ya han flasheado?) pasamos al día siguiente
#                   si hay repetimos...