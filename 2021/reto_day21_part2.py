
from anytree import Node, RenderTree, PreOrderIter, findall
victorias1=0
victorias2=0
def nuevaJugada(pl1,pl2,puntos1,puntos2):
    nuevasRamas=[]
    for i1 in range(1,4):
        for i2 in range(1,4):
            for i3 in range(1,4):
                for j1 in range(1,4):
                    for j2 in range(1,4):
                        for j3 in range(1,4):
                            player1=(pl1+i1+i2+i3)%10
                            player2=(pl2+j1+j2+j3)%10
                            if player1==0:
                                player1=10
                            if player2==0:
                                player2=10
                            puntos1=puntos1+player1
                            puntos2=puntos2+player2
                            if puntos1>=21:
                                victorias1+=1
                            elif puntos2>=21:
                                victorias2+=1
                            else:
                                (pl1,pl2,p1,p2)=nuevaJugada(player1,player2,puntos1,puntos2)
                            print("v1:"+str(victorias1))
                            jugada=(player1,player2,puntos1,puntos2,(i1,i2,i3),(j1,j2,j3))
                            nuevaRama=Node(jugada,padre)
                            nuevasRamas.append(nuevaRama)

player1=4#9
player2=8#10
puntos1=0
puntos2=0
jugada0=(player1,player2,puntos1,puntos2,(0,0,0),(0,0,0))
origen=Node(jugada0)
nuevasRamas=[]
# i2=1
# i3=1
# j1=1
# j2=1
# j3=1
for i1 in range(1,4):
    for i2 in range(1,4):
        for i3 in range(1,4):
            for j1 in range(1,4):
                for j2 in range(1,4):
                    for j3 in range(1,4):
                        pl1=origen.name[0]
                        pl2=origen.name[1]
                        player1=(pl1+i1+i2+i3)%10
                        player2=(pl2+j1+j2+j3)%10
                        if player1==0:
                            player1=10
                        if player2==0:
                            player2=10
                        puntos1=origen.name[2]+player1
                        if puntos1>=21:
                            victorias1+=1
                            print("v1:"+str(victorias1))
                        elif puntos2>=21:
                            victorias2+=1
                            print("v2:"+str(victorias2))
                        puntos2=origen.name[3]+player2
                        jugada=(player1,player2,puntos1,puntos2,(i1,i2,i3),(j1,j2,j3))
                        nuevaRama=Node(jugada,parent=origen)
                        nuevasRamas.append(nuevaRama)
i=0
while True:
    fin=True
    hojas=origen.leaves
    for hoja in hojas:
        if hoja.name[2]<21 and hoja.name[3]<21: 
            #nuevaJugada(hoja)
            padre=hoja
            nuevasRamas=[]
            # i2=1
            # i3=1
            # j1=1
            # j2=1
            # j3=1
            for i1 in range(1,4):
                for i2 in range(1,4):
                    for i3 in range(1,4):
                        for j1 in range(1,4):
                            for j2 in range(1,4):
                                for j3 in range(1,4):
                                    pl1=padre.name[0]
                                    pl2=padre.name[1]
                                    player1=(pl1+i1+i2+i3)%10
                                    player2=(pl2+j1+j2+j3)%10
                                    if player1==0:
                                        player1=10
                                    if player2==0:
                                        player2=10
                                    puntos1=padre.name[2]+player1
                                    puntos2=padre.name[3]+player2
                                    if puntos1>=21:
                                        victorias1+=1
                                        #print("v1:"+str(victorias1))
                                    elif puntos2>=21:
                                        victorias2+=1
                                        #print("v2:"+str(victorias2))
                                    if victorias1>30000:
                                        print(victorias1)
                                    jugada=(player1,player2,puntos1,puntos2,(i1,i2,i3),(j1,j2,j3))
                                    nuevaRama=Node(jugada,parent=padre)
                                    nuevasRamas.append(nuevaRama)
            fin=False
    if fin:
        print("FIN")
        break
    i+=1
    if i>100:
        print("Fin i")
        break
        
# for pre, fill, node in RenderTree(origen):
#     print("%s%s" % (pre, node.name))
    