#f = open("id9pru.txt", "r")
f = open("input9_2.txt", "r")
# def adyacentes2(matrix,x,y):
#     res=[]
#     if (y-1)>0 :
#         res.append(matrix[y-1][x])
#         if (x-1)>=0 :
#             res.append(matrix[y-1][x-1])
#         if (x+1)>=len(matrix[0]) :
#             res.append(matrix[y-1][x+1])
#     if (x-1)>=0 :
#         res.append(matrix[y][x-1])
#         if (y+1)>=len(matrix) :
#             res.append(matrix[y+1][x-1])
#             res.append(matrix[y+1][x])
#             if (x+1)>=len(matrix[0]):
#                 res.append(matrix[y+1][x+1])
#     return res

def adyacentes(matrix,x,y):
    res=[]
    if (x-1)>=0 :
        res.append(matrix[x-1][y])
    if (y-1)>=0 :
        res.append(matrix[x][y-1])
    if (x+1)<len(matrix) :
        res.append(matrix[x+1][y])
    if (y+1)<len(matrix[0]) :
        res.append(matrix[x][y+1])
    return res
input=f.read()
ilines=input.splitlines()
riskSum=0
for i in range(0,len(ilines)):
    for j in range(0,len(ilines[0])):
        #print(ilines[i][j])
        arr=adyacentes(ilines,i,j)
        if all(int(k) > int(ilines[i][j]) for k in arr):
            print(ilines[i][j],end='')
            risk=int(ilines[i][j])+1
            riskSum+=risk
            print(" risk: ",end='')
            print(risk)
print(" Total risk:")
print(riskSum)