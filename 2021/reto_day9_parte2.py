from anytree import Node, RenderTree, PreOrderIter, findall
import math

#f = open("id9pru.txt", "r")
f = open("input_day9.txt", "r")
# def adyacentes2(matrix,x,y):
#     res=[]
#     if (y-1)>0 :
#         res.append(matrix[y-1][x])
#         if (x-1)>=0 :
#             res.append(matrix[y-1][x-1])
#         if (x+1)>=len(matrix[0]) :
#             res.append(matrix[y-1][x+1])
#     if (x-1)>=0 :
#         res.append(matrix[y][x-1])
#         if (y+1)>=len(matrix) :
#             res.append(matrix[y+1][x-1])
#             res.append(matrix[y+1][x])
#             if (x+1)>=len(matrix[0]):
#                 res.append(matrix[y+1][x+1])
#     return res
def newElemEnBasin(arbol,arr):
    enArbol=findall(arbol, filter_=lambda node: node.name in arr)
    for nod in enArbol:
        arr.remove(nod.name)
    return arr

def adyacentes(matrix,x,y):
    res=[]
    if (x-1)>=0 :
        res.append(matrix[x-1][y])
    if (y-1)>=0 :
        res.append(matrix[x][y-1])
    if (x+1)<len(matrix) :
        res.append(matrix[x+1][y])
    if (y+1)<len(matrix[0]) :
        res.append(matrix[x][y+1])
    return res
def corAdyacentes(matrix,x,y):
    res=[]
    if (x-1)>=0 :
        if int(matrix[x-1][y])<9:
            res.append([x-1,y])
    if (y-1)>=0 :
        if int(matrix[x][y-1])<9:
            res.append([x,y-1])
    if (x+1)<len(matrix) :
        if int(matrix[x+1][y])<9:
            res.append([x+1,y])
    if (y+1)<len(matrix[0]) :
        if int(matrix[x][y+1])<9:
            res.append([x,y+1])
    return res
input=f.read()
ilines=input.splitlines()
riskSum=0
lowPoints=[]
for i in range(0,len(ilines)):
    for j in range(0,len(ilines[0])):
        #print(ilines[i][j])
        arr=adyacentes(ilines,i,j)
        if all(int(k) > int(ilines[i][j]) for k in arr):
            print(ilines[i][j],end='')
            risk=int(ilines[i][j])+1
            riskSum+=risk
            lowPoints.append([i,j])
            print(" risk: ",end='')
            print(risk)
lowPoints2=[lowPoints[2]]
basins=[]
for low in lowPoints:
    #Creamos un arbol desde ese elemento:
    basin=Node(low)
    adjs=corAdyacentes(ilines,low[0],low[1])
    for adj in adjs:
            Node(adj,parent=basin)
    
    # for pre, fill, node in RenderTree(basin):
    #     print("%s%s%s" % (pre, node.name, ilines[node.name[0]][node.name[1]]))
    while(True):
        #break
        #buscamos las hojas del arbol:
        hojas=basin.leaves
        #hojas=[]
        # for node in PreOrderIter(basin):
        #     if len(node.children)==0:
        #         hojas.append(node)
        noHayMasHijos=True
        for hoja in hojas:
            adjs=corAdyacentes(ilines,hoja.name[0],hoja.name[1])
            if (len(adjs)>0):
                restoAdjs=newElemEnBasin(basin,adjs)
            else:
                restoAdjs=[]
            if len(restoAdjs)>0:
                noHayMasHijos=False
        if noHayMasHijos:
            break
        else:
            for hoja in hojas:
                adjs=corAdyacentes(ilines,hoja.name[0],hoja.name[1])
                if (len(adjs)>0):
                    restoAdjs=newElemEnBasin(basin,adjs)
                else:
                    restoAdjs=[]
                for adj in restoAdjs:
                        Node(adj,parent=hoja)
    basins.append(basin)
    print(len(basin.descendants)+1)
    #ESTO PARA ESTUDIAR A FONDO LAS BASINS,
    #Para tener solo los tamaños maximos nos basta con lo siguiente:
    # tam=[]
    # for i in range(0,len(basins)):
    #     tam.append([i,len(basins[i].descendants)+1])
    # mayores=sorted(tam,key=lambda x:x[1])[-3:]
    # mayorBasins=[]
    # for j in range(len(mayores)):
    #     mayorBasins.append(basins[mayores[j][0]])
    
tam=[]
for i in range(0,len(basins)):
    tam.append(len(basins[i].descendants)+1)
mayores=sorted(tam)[-3:]
print("RESULTADO:")
print(math.prod(mayores))


#1. parto de un low point [5] y añado sus coordenadas a la basin:
#2. busco todos sus adyacentes [8,8,6,6] y añado sus coordenadas a la basin, si no son 9
#3. para cada adyacente busco sus adyacentes que no sean 9 y no esten ya en la basin [8:7,8:7,6:7,6:7] y añado sus coordenadas a la basin
#4. para cada nuevo adyacente busco

#Para cada low point:
# busco sus hijos: adyancentes que no sean 9 y los meto en un arbol
# Exploro los extremos del arbol: tienen hijos distintos de 9 que no esten en el arbol? si no, hemos acabado, si tienen:
# busco los hijos de esos hijos: adyacentes de estos que no sean 9 y no esten ya en el arbol 
    