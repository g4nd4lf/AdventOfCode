
player1=9
player2=10
def lanzaDado(pos,i):
    newPos=(pos+i*9+6) % 10
    if newPos==0:
        newPos=10
    return(newPos)
puntos1=0
puntos2=0
# print("player1: "+str(player1))
# print("player2: "+str(player2))
# print("puntos1: "+str(puntos1))
# print("puntos2: "+str(puntos2))
i=0
while True: 
    player1=lanzaDado(player1,i)
    puntos1+=player1
    if puntos1>=1000:
        break
    i+=1
    player2=lanzaDado(player2,i)
    puntos2+=player2
    if puntos2>=1000:
        break
    print("player1: "+str(player1))
    print("player2: "+str(player2))
    print("puntos1: "+str(puntos1))
    print("puntos2: "+str(puntos2))
    i+=1
print(puntos2)
puntosSegundo=min([puntos1,puntos2])
tiradas=3*(i+1)
print("Parte 1: "+str(tiradas*puntosSegundo))