import re
#Patron original:
patron={'abcefg':0,'cf':1,'acdeg':2,'acdfg':3,'bcdf':4,'abdfg':5,'abdefg':6,'acf':7,'abcdefg':8,'abcdfg':9}
segmento=['a','b','c','d','e','f','g']
#f = open("id8pru.txt", "r")
#f = open("id8pru_parte2.txt", "r")
f = open("input_day8.txt", "r")
input=f.read()
ilines=input.splitlines()
codigo=[]
mensaje=[]
patronList=list(patron.keys())
cero=patronList[0]
uno=patronList[1]
dos=patronList[2]
tres=patronList[3]
cuatro=patronList[4]
cinco=patronList[5]
seis=patronList[6]
siete=patronList[7]
ocho=patronList[8]
nueve=patronList[9]
ilines2=[ilines[0]]
sumaResultado=0
for line in ilines:
    print(line)
    dic={}
    codigo=line.split("|")[0]
    palabras=codigo.split(" ")
    palabras.pop()
    mensaje=line.split("|")[1]
    for cod in palabras:
        #print(len(cod))
        if(len(cod)==2):
            uno=cod #1
        elif(len(cod)==3):
            siete=cod #2
        elif(len(cod)==4):
            cuatro=cod
        elif(len(cod)==7):
            ocho=cod
    #3
    for c in siete:
        #print(c)
        if c not in uno:
            dic[c]='a' #segmento[0]=c #3
    #4. Las letras del 1 (ej ab) me permiten identificar el numero 3: 
    # El 3 será aquel de longitud 5 que contenga esas letras (ab) osea 3:fbcad
                      
    for cod in palabras:
        if(len(cod)==5 and (uno[0] in cod) and (uno[1] in cod)):
            tres=cod
    #5
    for c in cuatro:
        if(c not in tres):
            dic[c]='b'#segmento[1]=c
    #6
    c1=list(dic.keys())[list(dic.values()).index('b')]
    for c in cuatro:
        if (c not in uno) and (c is not c1):
            dic[c]='d'#segmento[3]=c
    #7. De los numeros de 5 segmentos que quedan (ya hemos encontrado el 3), el 5 será el que contenga el segmento superior izquierdo (e)
    for cod in palabras:
        if(len(cod)==5 and (cod is not tres) and (c1 in cod)):
            cinco=cod
    #8
    for cod in palabras:
        if (len(cod)==5 and (cod is not tres) and (cod is not cinco)):
            dos=cod
    #9
    for c in uno:
        if c in cinco:
            dic[c]='f'#segmento[5]=c
        else:
            dic[c]='c'#segmento[2]=
    #[identificados: a,b,c,d,f]
    #10. Si quitamos los segmentos ya identificados (d,f y las dos letras del 1,ab) en el numero 5 y en el 2, 
    #   la letra comun que queda es el segmento inferior (c):c->g
    c0=list(dic.keys())[list(dic.values()).index('a')]
    c1=list(dic.keys())[list(dic.values()).index('b')]
    c3=list(dic.keys())[list(dic.values()).index('d')]
    c5=list(dic.keys())[list(dic.values()).index('f')]
    for c in cinco:
        if (c not in [c0,c1,c3,c5]):
            dic[c]='g'#segmento[6]=c
            print(c)
    #11
    for c in ['a','b','c','d','e','f','g']:
        if c not in list(dic.keys()):
            dic[c]='e'#segmento[4]=''
            #segmento[4]=c
    palabrasMensaje=mensaje.split(' ')
    del palabrasMensaje[0]
    codigoTxt=""
    for m in palabrasMensaje:
        #mensaje decodificado (md)
        md=""
        for c in m:
            md=md+dic[c]
        md=''.join(sorted(md))
        #print(md)
        #print(patron[md])
        codigoTxt=codigoTxt+str(patron[md])
    codigoNumerico=int(codigoTxt)
    sumaResultado+=codigoNumerico
print(sumaResultado)




#1. Busco el 1 (long2): ab
#2. busco el 7 (long3): dab
#3. Resto las letras del 1 al 7: d ->ese es el segmento superior: d->a
#4. Las letras del 1 (ej ab) me permiten identificar el numero 3: 
    # El 3 será aquel de longitud 5 que contenga esas letras (ab) osea 3:fbcad
#5. La letra del numero 4 (eafb) que no este en el 3 sera la del segmento superior izquierdo: e->b
#6. Si quito esa letra del numero 4 y las letras del 1 (ab),la que nos queda (f) es el segmento central:f->d
#7. De los numeros de 5 segmentos que quedan (ya hemos encontrado el 3), el 5 será el que contenga el segmento superior izquierdo (e)
#8. El 2 será el que queda de 5 segmentos
#9. De las dos letras del 1 (ab), la que se encuentre en el 5 sera el segmento inferior derecho (f) y la otra el segmento superior derecho (c)
#10. Si quitamos los segmentos ya identificados (d,f y las dos letras del 1,ab) en el numero 5 y en el 2, 
#   la letra comun que queda es el segmento inferior (c):c->g
#11.La letra que falta por identificar (g) será el segmento inferior izquierdo: g->e [a,b,c,d,e,f,g]
