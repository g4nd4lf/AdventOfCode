#import pandas as pd
import os
os.chdir("./2023/day3")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'
# def findNumbers(str):
#     numbers=[]
#     number=""
#     for c in str:
#         if c.isdigit():
#             number+=c
#         elif len(number)>0:
#             numbers.append(int(number))
#             number=""
#     return numbers
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
        
with open(input1) as f:
    lines = f.readlines()
    numbers=[]
    number=""
    symbol=False
    j=0
    for l in lines:
        i=0
        for i,c in enumerate(l):
            if c.isdigit():
                number+=c
                if some_neighbour_symbols(lines,i,j):
                    symbol=True
            elif len(number)>0 and symbol:
                numbers.append(int(number))
                number=""
                symbol=False
            elif len(number)>0:
                number=""
            i+=1
        j+=1
    #return numbers
    #result=findNumbers(lines[0])
    #lines[0]=
    #result=0
    #for l in lines:

print(numbers,sum(numbers))