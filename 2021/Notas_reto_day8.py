#f = open("id8pru.txt", "r")
from io import DEFAULT_BUFFER_SIZE


f = open("input_day8.txt", "r")
input=f.read()
ilines=input.splitlines()
codigo=[]
mensaje=[]
for line in ilines:
    codigo.append(line.split("|")[0])
    mensaje.append(line.split("|")[1])
print(mensaje)
contador=0
for m in mensaje:
    palabras=m.split(' ')
    for p in palabras:
        #las longitudes de palabra unicas son 2,4,3,7 (que se correspoenden a los digitos 1,4,7 y 8)
        if (len(p)== 2 or len(p)==3 or len(p)==4 or len(p)==7):
            contador=contador+1
print(contador)

1:ab
7:dab
4:eafb

#Patron original:
patron=[['abcefg'],['cf'],['acdeg'],['acdfg'],['bcdf'],['abdfg'],['abdefg'],['acf'],['abcdefg'],['abcdfg']]


#Busco el 1 (long2): ab
#busco el 7 (long3): dab
#Resto las letras del 1 al 7: d ->ese es el segmento superior: d->a
#Las letras del 1 (ej ab) me permiten identificar el numero 3: 
    # El 3 será aquel de longitud 5 que contenga esas letras (ab) osea 3:fbcad
#La letra del numero 4 (eafb) que no este en el 3 sera la del segmento superior izquierdo: e->b
#Si quito esa letra del numero 4 y las letras del 1 (ab),la que nos queda (f) es el segmento central:f->b
#De los de 5 segmentos que quedan (ya hemos encontrado el 3), el 5 será el que contenga el segmento superior izquierdo (e)
#El 2 será el que queda de 5 segmentos
#De las dos letras del 1 (ab), la que se encuentre en el 5
#Si quitamos los segmentos ya identificados (d,f y las dos letras del 1,ab) en el numero 5 y en el 2, la letra comun que queda es el segmento inferior (c):c->g
#Si quitamos la letra encontrada a las letras que nos quedan del 5 la letra restante (b) es el segmento inferior derecho: f->b [d,e,f,c,b]
#La otra letra del 1, restando la encontrada (b) sera el segmento superior derecho (a): c->a [a,b,c,d,e,f]
#La letra que falta por identificar (g) será el segmento inferior izquierdo: g->e [a,b,c,d,e,f,g]

{
'd': 'a', 
'g': 'd', 
'c': 'g', 
'b': 'f', 
'e': 'c', 
'a': 'e', 
'f': 'e'}

'd': 'g', 
'g': 'b', 
'c': 'd', 
'b': 'c', 
'e': 'f', 
'f': 'g', 
'a': 'e'

longitudes:
0-6
1-2
2-5
3-5
4-4
5-5
6-6
7-3
8-7
9-6

2,3,4,7, 5,5,5, 6,6,6  

5 segmentos tienen: 2,3,5
6 segmentos tienen: 0,6,9


