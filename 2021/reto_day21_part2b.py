
from functools import lru_cache

def tirada(pos,ptos,tirada):
    newPos=((pos+tirada-1)%10)+1
    ptos+=newPos
    return(newPos,ptos)

@lru_cache(maxsize=None)
def jugada(player,pl1,pt1,pl2,pt2):
    if pt1>=21:
        return (1,0)
    elif pt2>=21:
        return (0,1)
    victorias=[0,0]
    for i1 in range(1,4):
        for i2 in range(1,4):
            for i3 in range(1,4):
                if not player:
                    (npl1,npt1)=tirada(pl1,pt1,i1+i2+i3)
                    (w1,w2)=jugada(1,npl1,npt1,pl2,pt2)
                else:
                    (npl2,npt2)=tirada(pl2,pt2,i1+i2+i3)
                    (w1,w2)=jugada(0,pl1,pt1,npl2,npt2)       
                victorias[0]+=w1
                victorias[1]+=w2
    return victorias

print(max(jugada(0,9,0,10,0)))
