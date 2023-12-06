from os import walk
from anytree import Node, RenderTree, PreOrderIter, findall_by_attr, Walker
w=Walker()


def calculaRutasPosibles(arbol):
    rutasPosibles=[]
    for node in PreOrderIter(arbol):
        print("ini:")
        print(node)
        for ni in PreOrderIter(node):
            if ni!=node:
                print("fin:")
                print(ni)
                print("ruta:")
                print(ruta(node,ni))
                rutasPosibles.append(ruta(node,ni))
    print("rutas posibles: "+str(len(rutasPosibles)))
    return rutasPosibles

def rutasPosiblesDesde(todasRutas,posOcupadas,nodo):
    rpd=[]
    posOcupadas.remove(nodo)
    for r in todasRutas:
        if(r[0]==nodo and not any(i in r for i in posOcupadas)):
            rpd.append(r)
    return rpd

def pA(arbol):
    """"Imprime el arbol"""
    for pre, fill, node in RenderTree(arbol):
        print("%s%s" % (pre, node.name))
def ruta(ini,fin):
    ruta=[]
    for r in w.walk(ini,fin):
        if type(r)==tuple:
            for r2 in r:#if (len(r)>=1):
                ruta.append(r2.name)
        else:
            ruta.append(r.name)
    return ruta

#Construccion del arbol que simula la geometria:
#Hall
n0=Node([0,0])
n1=Node([0,1],n0)
n2=Node([0,2],n1)
n3=Node([0,3],n2)
n4=Node([0,4],n3)
n5=Node([0,5],n4)
n6=Node([0,6],n5)
n7=Node([0,7],n6)
n8=Node([0,8],n7)
n9=Node([0,9],n8)
n10=Node([0,10],n9)
#RoomA
n11=Node([1,2],n2)
n12=Node([2,2],n11)
#RoomB
n13=Node([1,4],n4)
n14=Node([2,4],n13)
#RoomC
n15=Node([1,6],n6)
n16=Node([2,6],n15)
#RoomD
n17=Node([1,8],n8)
n18=Node([2,8],n17)

#Imprime el arbol
pA(n0)

#calcula rutasPosibles
rutasPosibles=calculaRutasPosibles(n0)

matrix=[]
f = open("input_day23.txt", "r")
input=f.read()
ilinesS=input.splitlines()
ilinesS.pop(0)
ilinesS.pop(-1)
matrix.append(list(ilinesS[0][1:-1]))
matrix.append(list(ilinesS[1][1:-1]))
matrix.append(list("#"+ilinesS[2][2:-1]+"##"))

#Calculo de las posibles posiciones recorriendo el arbol
positions=[]
for pre, fill, node in RenderTree(n0):
        positions.append(node.name)
print(positions)

#Calculo alternativo de las posibles posiciones, a partir de la matriz
# positions=[]
# for i in range(3):
#     for j in range(11):
#         if (matrix[i][j]!="#"):
#             positions.append([i,j])            
# print(positions)            
noStopPos=[[0,2],[0,4],[0,6],[0,8]]

posOcupadas=[]
posLibres=[]
amphipods=['A','B','C','D']
for p in positions:
    if (matrix[p[0]][p[1]] in amphipods):
        posOcupadas.append(p) 
    elif(matrix[p[0]][p[1]]=='.'):
        posLibres.append(p)


posiblesMovimientos=[]
for p in posOcupadas:
    posiblesMovimientos.append(rutasPosiblesDesde(rutasPosibles,posOcupadas,p))
    #por cada posible hago un movimiento, vuelvo a ver los posibles movimientos, por cada posible hago un movimiento....

# rutas1=[[[1,2],[0,2],[0,1],[0,0]],
#        [[1,2],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10]],
#        [[2,2],[1,2],[0,2],[0,1],[0,0]],
#        [[2,2],[1,2],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10]],
#        [[1,4],[0,4],[0,3],[0,2],[0,1],[0,0]],
#        [[1,4],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10]],
#        [[2,4],[1,4],[0,4],[0,3],[0,2],[0,1],[0,0]],
#        [[2,4],[1,4],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10]],
#        [[1,6],[0,6],[0,5],[0,4],[0,3],[0,2],[0,1],[0,0]],
#        [[1,6],[0,6],[0,7],[0,8],[0,9],[0,10]],
#        [[2,6],[1,6],[0,6],[0,5],[0,4],[0,3],[0,2],[0,1],[0,0]],
#        [[2,6],[1,6],[0,6],[0,7],[0,8],[0,9],[0,10]],
#        [[1,8],[0,8],[0,7],[0,6],[0,5],[0,4],[0,3],[0,2],[0,1],[0,0]],
#        [[1,8],[0,8],[0,9],[0,10]],
#        [[2,8],[1,8],[0,8],[0,7],[0,6],[0,5],[0,4],[0,3],[0,2],[0,1],[0,0]],
#        [[2,8],[1,8],[0,8],[0,9],[0,10]]
#        ]
# rutas=[]
# for r in rutas1:
#     rutas.append(r)
#     rutas.append(r[-1::-1])

# def p(matrix):
#     for m in matrix:
#         print(m)
# def p2():
#     print("###############")
#     print('##'+''.join(matrix[0])+'##')
#     print('  '+''.join(matrix[1])+'  ')
#     print('  '+''.join(matrix[2])+'  ')
#     #for i in range(len(matrix)):
#     #    print('##'+''.join(matrix[i])+'##')
#         #print(matrix)
# def mov(ini,fin):
#     matrix[fin[0]][fin[1]]=matrix[ini[0]][ini[1]]
#     matrix[ini[0]][ini[1]]='.'
# def esPosible(ini,fin):
#     if ini not in positions:
#         return False
#     elif fin not in positions:
#         return False
#     elif fin in noStopPos:
#         return False
#     else:
#         return True
# #p2(matrix)
# #p2()
# n=[]
# n.append(Node([0,0]))

# for i in range(3):
#     for j in range(11):
#         if (matrix[i][j]!="#"):
#             positions.append([i,j])
#             if not(i==0 and j==0):
#                 n.append(Node([i,j]))
                
# #print(positions)
# noStopPos=[[0,2],[0,4],[0,6],[0,8]]
# roomA=[[1,2],[2,2]]
# roomB=[[1,4],[2,4]]
# roomC=[[1,6],[2,6]]
# roomD=[[1,8],[2,8]]
# mov(roomA[0],[0,1])
#print()
#p2(matrix)
#p2()
#print(esPosible(roomA[0],[0,1]))
#print(esPosible(roomA[0],[1,1]))
