def leeDatos(file):
    f = open(file, "r")
    input=f.read()
    ilinesS=input.split("\n")
    mat=[]
    for i in range(len(ilinesS)):
        linea=[]
        for j in range(len(ilinesS[0])):
            linea.append(ilinesS[i][j])
        mat.append(linea)
    return(mat)

paper0=leeDatos("paper0.txt")