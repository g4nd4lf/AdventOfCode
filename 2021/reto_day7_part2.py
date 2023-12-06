def contarEnArray(arr,elem):
    """Función que cuenta el numero de veces que aparece el elemento elem en el array arr"""
    conteo=0
    for i in arr:
        if (i==elem):
            conteo=conteo+1
    return conteo
#f = open("id7pru.txt", "r")
f = open("input_day7.txt", "r")
input=f.read()
ini=input.split(",")
crabs=[int(x) for x in ini]
minC=min(crabs)
maxC=max(crabs)
posiciones=[]
for i in range(0,maxC+1):
    posiciones.append(0)
for j in range(minC,maxC+1):
    posiciones[j]=contarEnArray(crabs,j)
minCoste=10000000000
posMin=0
for k in range(minC,maxC+1):
    coste=0
    for l in range(minC,maxC+1):
        coste=coste+(0.5*abs(k-l)+0.5*abs(k-l)*abs(k-l))*posiciones[l]
        # if (k==2):
        #     costei=0.5*abs(k-l)+0.5*abs(k-l)*abs(k-l)*posiciones[l]
        #     print(costei)
    if (coste<minCoste):
        minCoste=coste
        posMin=k
    #print(k)
    #print(coste)
print("coste minimo:")
print(minCoste)
print("posición minima:")
print(posMin)