import os
os.chdir("./day13")
#input1='sample.txt'
input1='input.txt'

def mirror(pattern,idx):
    j=idx-1
    for i in range(idx,len(pattern)):
        if j>=0:
            if pattern[i]!=pattern[j]:
                return False
        j-=1
    return True
    
def transpose(pattern):
    transpuesto = list(zip(*pattern))
    newpattern=[]
    for fila in transpuesto:
        newpattern.append(''.join(fila))
    return newpattern

def count_score(pattern):
    for i in range(len(pattern)-1):
        if pattern[i+1]==pattern[i]:
            if mirror(pattern,i+1):
                return 100*(i+1)
    pattern=transpose(pattern)
    for i in range(len(pattern)-1):
        if pattern[i+1]==pattern[i]:
            if mirror(pattern,i+1):
                return i+1
    return 0
    


patterns=[]
print("Reading and parsing data:")
result=0
with open(input1) as f:
    lines=f.readlines()
    pattern=[]
    for i,l in enumerate(lines):
        print(l)        
        l=l.replace("\n","")
        l=l.replace(".","0")
        l=l.replace("#","1")
        if l=="":
            patterns.append(pattern)
            result+=count_score(pattern)
            pattern=[]
            
        else:
            pattern.append(l)
    
        #print(number_of_valid_combination)
    patterns.append(pattern)
    #pattern=[]
    result+=count_score(pattern)
    
    print("result:",result)
