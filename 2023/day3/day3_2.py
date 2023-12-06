#import pandas as pd
import os
os.chdir("./2023/day3")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'
def findNumbers(matrix):
    numbers=[]
    coors=[]
    for j,line in enumerate(matrix):
        number=""
        coor=[]
        for i,c in enumerate(line):
            if c.isdigit():
                number+=c
                coor.append((i,j))
            elif len(number)>0:
                numbers.append((int(number),coor))
                number=""
                coor=[]
    
    return numbers
def find_asterisks(matrix):
    asterisks=[]
    for j in range(len(matrix)):
        for i in range(len(matrix[0])-1):
            if matrix[j][i]=="*":
                asterisks.append((i,j))
    return asterisks

def some_neighbour_symbols(matrix,i,j):
    neighbours=((i-1,j),(i-1,j-1),(i-1,j+1),
                (i,j-1),(i,j+1),
                (i+1,j-1),(i+1,j),(i+1,j+1))
    for n in neighbours:
        if n[0]>=0 and n[0]<len(matrix[0]) and n[1]>=0 and n[1]<len(matrix) :
            ch=matrix[n[1]][n[0]]
            is_symbol=  ch !="." and not ch.isdigit() and ch!="\n"
            if is_symbol:
                return True
    return False

def is_neighbour(coord1,coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    # Calcula las diferencias en las coordenadas
    diff_x = abs(x1 - x2)
    diff_y = abs(y1 - y2)

    # Verifica si las coordenadas son vecinas en alguna dirección
    is_neighbour = (diff_x == 1 and diff_y == 0) or (diff_x == 0 and diff_y == 1) or (diff_x == 1 and diff_y == 1)

    return is_neighbour
def neighbour_numbers(coor,numbers):
    pair=[]
    for n in numbers:
        for c in n[1]:
            if is_neighbour(coor,c):
                if len(pair)==0:
                    pair.append(n[0])
                    break
                else:
                    return (pair[0],n[0])
    return -1
            
with open(input1) as f:
    lines = f.readlines()
    numbers=findNumbers(lines)
    asterisks=find_asterisks(lines)
    result=0
    for a in asterisks:
        neighbours=neighbour_numbers(a,numbers)
        if neighbours !=-1:
            product=neighbours[0]*neighbours[1]
            result+=product
    
print(result)