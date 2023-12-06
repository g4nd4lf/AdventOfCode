from os import walk
from anytree import Node, RenderTree, PreOrderIter, findall_by_attr, Walker
    
matrix=[]
matrix.append(['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'])
matrix.append(['#', '#', 'A', '#', 'C', '#', 'C', '#', 'D', '#', '#'])
matrix.append(['#', '#', 'B', '#', 'D', '#', 'A', '#', 'B', '#', '#'])
casaini=['.']*11+['A','B','C','D','C','A','D','B']
casa=['.']*11+['A','B','C','D','C','A','D','B']
amphipods=['A','B','C','D']
noStopPos=[2,4,6,8]
hall=list(range(11))
casaFinal=['.']*11+['A','A','B','B','C','C','D','D']
roomFinal=['.']*11+['A','A','B','B','C','C','D','D']
roomAi=[11,12]
roomBi=[13,14]
roomCi=[15,16]
roomDi=[17,18]
roomsi=[roomAi,roomBi,roomCi,roomDi]
irooms={'A':[11,12],'B':[13,14],'C':[15,16],'D':[17,18]}

roomA=casa[roomAi[0]:roomAi[1]]
roomB=casa[roomBi[0]:roomBi[1]]
roomC=casa[roomCi[0]:roomCi[1]]
roomD=casa[roomDi[0]:roomDi[1]]
a=[11,16]
b=[12,18]
c=[13,15]
d=[14,17]
posLibres=hall.copy()
posOcupadas=list(range(11,19))
roomUp=[11,13,15,17]
roomDown=[12,14,16,18]

#Construccion del arbol que simula la geometria:
#Hall
n=[]
n.append(Node(0))

for i in range(1,11):
    n.append(Node(1,n[i-1]))
#RoomA
n.append(Node(11,n[2]))
n.append(Node(12,n[11]))
#RoomB
n.append(Node(13,n[4]))
n.append(Node(14,n[13]))
#RoomC
n.append(Node(15,n[6]))
n.append(Node(16,n[15]))
#RoomD
n.append(Node(17,n[8]))
n.append(Node(18,n[17]))

# n1=Node(1,n0)
# n2=Node(2,n1)
# n3=Node(3,n2)
# n4=Node(4,n3)
# n5=Node(5,n4)
# n6=Node(6,n5)
# n7=Node(7,n6)
# n8=Node(8,n7)
# n9=Node(9,n8)
# n10=Node(10,n8)
# #RoomA
# n11=Node(11,n2)
# n12=Node(12,n11)
# #RoomB
# n13=Node(13,n4)
# n14=Node(14,n13)
# #RoomC
# n15=Node(15,n6)
# n16=Node(16,n15)
# #RoomD
# n17=Node(17,n8)
# n18=Node(18,n17)

w=Walker()
def roomIni(i):
    if casa[i]=='A':
        return 0
    if casa[i]=='B':
        return 1
    if casa[i]=='C':
        return 2
    if casa[i]=='D':
        return 3
    else:
        return -1
def room(i):
    """nos dice el nombre de la room correspondiente a ese inidice i"""
    return roomFinal[i]
def noEsmiRoom(ini,fin):
    if fin in hall:
        return False
    else:
        return (casa[ini]!=room(fin))
def roomOcupada(fin):
    #si en la room de fin hay una letra que no esta en su casa
    if fin in hall:
        return False
    else:
        roomOcupada=False
        for i in irooms[room(fin)]:
            if casa[i]!=room(fin):
                roomOcupada=True
        return roomOcupada

def rutaOld(ini,fin):
    ruta=[]
    for r in w.walk(n[ini],n[fin]):
        if type(r)==tuple:
            for r2 in r:#if (len(r)>=1):
                ruta.append(r2.name)
        else:
            ruta.append(r.name)
    return ruta

def rutaOcupada(ini,fin):
    r=ruta(ini,fin)
    restoRuta=r.copy()
    restoRuta.remove(ini)
    return not set(restoRuta).isdisjoint(posOcupadas)

def movOk(ini,fin):
    movOk=True
    if (fin in noStopPos) or rutaOcupada(ini,fin):
        movOk=False
    if roomOcupada(fin) or noEsmiRoom(ini,fin) :
        movOk=False
    if ini in hall and fin in hall:
        movOk=False
    return movOk

def posiblesMov():
    posiblesMovimientos=[]
    for ini in posOcupadas:
        for fin in posLibres:
            if movOk(ini,fin):
                posiblesMovimientos.append([ini,fin])
    return posiblesMovimientos

def inicializar():
    f = open("input_day23.txt", "r")
    input=f.read()
    ilinesS=input.splitlines()
    ilinesS.pop(0)
    ilinesS.pop(-1)
    matrix.append(list(ilinesS[0][1:-1]))
    matrix.append(list(ilinesS[1][1:-1]))
    matrix.append(list("#"+ilinesS[2][2:-1]+"##"))

def mov(ini,fin):
    if movOk(ini,fin):
        casa[fin]=casa[ini]
        casa[ini]='.'
        actualiza()

def actualiza():
    posOcupadas=[]
    posLibres=[]
    for i in range(len(casa)):
        if casa[i]=='.':
            posLibres.append(i)
        else:
            posOcupadas.append(i)


def pA(arbol):
    """"Imprime el arbol"""
    for pre, fill, node in RenderTree(arbol):
        print("%s%s" % (pre, node.name))
def ruta(ini,fin):
    ruta=[]
    for r in w.walk(n[ini],n[fin]):
        if type(r)==tuple:
            for r2 in r:#if (len(r)>=1):
                ruta.append(r2.name)
        else:
            ruta.append(r.name)
    return ruta

def p(matrix):
    for m in matrix:
        print(m)

def pr2():
    casaini=['.']*11+['A','B','C','D','C','A','D','B']
    
    print("#############")
    print('#'+''.join(casa[0:11])+'#')
    print('###'+casa[11]+'#'+casa[13]+'#'+casa[15]+'#'+casa[17]+'###')
    print('  #'+casa[12]+'#'+casa[14]+'#'+casa[16]+'#'+casa[18]+'###')
    print("  #########  ")

inicializar()
pms=[]  #pms[0] guarda los posibles movimientos en 1ª fase
historico=[]
# def nuevoMovimiento():
#     if posibles
#     for m in posiblesMov():
#         mov(m[0],m[1])
#         historico.append(m)
soluciones=[]
arbol=Node(([0,0],0))
p=posiblesMov()
casas=[]
k=0
casas.append(casa.copy())
for m in p:
    Node((m,0),parent=arbol)
fin=False
while(True):
    hojas=arbol.leaves
    noHayMasMovimientos=True
    pTotal=[]
    for hoja in hojas:
        m2=hoja.name[0]
        casa=casas[hoja.name[1]]
        mov(m2[0],m2[1])
        pr2()
        fin=True
        if (casa==casaFinal):
            print("Encontrada solucion")
            soluciones.append(hoja)
            continue
        p2=posiblesMov()
        k+=1
        casas.append(casa.copy())
        if (len(p2)>0):
            noHayMasMovimientos=False
            for m2 in p2:
                Node((m2,k),parent=hoja)
        #print(hoja.name)
        #break
        # mov(m[0],m[1])
        # if (casa==casaFinal):
        #     print("Encontrada solucion")
        #     soluciones.append(ramas[-1])
        #     break
        # else: 
        #     p2=posiblesMov()
        #     if (len(p2)==0):
        #         print("no hay más movimientos. Solución no encontrada")
        #         #retroceder un paso en el arbol y elegir otro movimiento

    
        # for m2 in posiblesMov():
        #     mov(m2[0],m2[1])
        #     roomFinal=['.']*11+['A','A','B','B','C','C','D','D']

        # if casa==casaFinal:
    if noHayMasMovimientos or fin:
        break
    #else:

print("FIN")






#
# 
#  print(matrix[0])
# print(matrix[1])
# print(matrix[2])
#Calculo de las posibles posiciones recorriendo el arbol
# positions=[]
# for pre, fill, node in RenderTree(n0):
#         positions.append(node.name)
# print(positions)

#Calculo alternativo de las posibles posiciones, a partir de la matriz
# positions=[]
# for i in range(3):
#     for j in range(11):
#         if (matrix[i][j]!="#"):
#             positions.append([i,j])            
# print(positions)            



# print("ocupadas1:")
# print(posOcupadas)
# #rpru=rutasPosiblesDesde(rutasPosibles,posOcupadas,[1,2])
# #print(rpru)
# actualizaPosiciones()
# posiblesMovimientos=[]
# for p in posOcupadas:
#     posiblesMovimientos+=(rutasPosiblesDesde(rutasPosibles,posOcupadas,p))
# print("pm: "+str(len(posiblesMovimientos)))
    
# for pm in posiblesMovimientos:
#     mov(pm[0],pm[-1])
#     actualizaPosiciones()
#     posiblesMovimientos2=[]
#     for p2 in posOcupadas:
#         posiblesMovimientos2+=(rutasPosiblesDesde(rutasPosibles,posOcupadas,p2))
#     print("pm2: "+str(len(posiblesMovimientos2)))
#     #for pm2 in posiblesMovimientos:

# print("ocupadas2:")
# print(posOcupadas)

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


    
    #for i in range(len(matrix)):
    #    print('##'+''.join(matrix[i])+'##')
        #print(matrix)
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
# mov(roomA[0],[0,1])
#print()
#p2(matrix)
#p2()
#print(esPosible(roomA[0],[0,1]))
#print(esPosible(roomA[0],[1,1]))
