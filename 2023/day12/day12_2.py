import os

os.chdir("./day12")
input1='sample.txt'
#input1='input.txt'
class Node:
    def __init__(self, data):
        self.data = 0
        self.leftChild = None
        self.rightChild = None
    def insert(self, data):
        self.leftChild=Node()
    def 
def idx(s, c):
    return [i for i, char in enumerate(s) if char == c]

def is_posible(str,code):
    datacode=[len(uno) for uno in str.split('0') if uno]
    if len(datacode)>len(code):
        return False
    pass
    for i in range(len(datacode)-1):
        if datacode[i]!=code[i]:
            return False
    return True
def find_all_combinations(idxs):
    binarios=[]
    for i in range(2**len(idxs)):
        binario = format(i, f'0{len(idxs)}b')
        binarios.append(binario)
    combos=[]
    for bin in binarios:
        combi={}
        for i,b in enumerate(bin):
            combi[idxs[i]]=int(b)
        combos.append(combi)
    return combos

def match_code(data,code):
    s=data.split(".")
    data_code=[len(x) for x in s if '#' in x]
    return data_code==code

def unfold(data,code):
    newdata=(data+"?")*5
    newcode=(code+",")*5
    return newdata[:-1], newcode[:-1]

print("Reading and parsing data:")
with open(input1) as f:
    lines=f.readlines()
    total=0
    for i,l in enumerate(lines):
        print(i)        
        l=l.replace("\n","")
        data,code_string=l.split(" ")
        data,code_string=unfold(data,code_string)
        code=[int(x) for x in code_string.split(",")]
        groups=len(code)
        dudes=idx(data,"?")
        data2=data.replace('.','0')
        data2=data2.replace('#','1')
        while 


        combinations=find_all_combinations(data2,dudes)
        number_of_valid_combination=0
        for combi in combinations:
            data=data2
            posible=True
            for c in combi:
                data=data[:c]+str(combi[c])+data[c+1:]
                if not is_posible(data.split("?")[0],code):
                    posible=False
                    break
            if posible:
                if code==[len(uno) for uno in data.split('0') if uno]:
                    number_of_valid_combination+=1
                    total+=1
                    #print(i,combi,number_of_valid_combination)
                
    print("total:",total)
