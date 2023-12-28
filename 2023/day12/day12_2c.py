import os

os.chdir("./day12")
#input1='sample.txt'
input1='input.txt'

def idx(s, c):
    return [i for i, char in enumerate(s) if char == c]

def find_all_combinations(idxs,code):
    binarios=[]
    for i in range(2**len(idxs)):
        binario = format(i, f'0{len(idxs)}b')
        if [len(uno) for uno in b.split('0') if uno] == code:
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

print("Reading and parsing data:")
with open(input1) as f:
    lines=f.readlines()
    total=0
    for i,l in enumerate(lines):
        print(i)        
        l=l.replace("\n","")
        data,code_string=l.split(" ")
        code=[int(x) for x in code_string.split(",")]
        groups=len(code)
        dudes=idx(data,"?")
    

        combinations=find_all_combinations(dudes,code)
        number_of_valid_combination=0
        for combi in combinations:
            datai=list(data)
            for c in combi:
                datai[c]='#' if combi[c] else '.'
            dataStr=''.join(datai)
            if match_code(dataStr,code):
                number_of_valid_combination+=1
                total+=1
        #print(number_of_valid_combination)
    
    print("total:",total)
