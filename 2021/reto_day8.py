#f = open("id8pru.txt", "r")
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