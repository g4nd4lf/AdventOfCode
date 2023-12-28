import os, copy
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
    #if j>=0:
    #    return False
    return True
    
def transpose(pattern):
    transpuesto = list(zip(*pattern))
    newpattern=[]
    for fila in transpuesto:
        newpattern.append(''.join(fila))
    return newpattern
def find_posible_axis(pattern):
    idxs=[]
    for i in range(len(pattern)-1):
        if pattern[i+1]==pattern[i]:
            pass

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
#result=0
with open(input1) as f:
    lines=f.readlines()
    pattern=[]
    for i,l in enumerate(lines):
        #print(l)        
        l=l.replace("\n","")
        l=l.replace(".","0")
        l=l.replace("#","1")
        if l=="":
            patterns.append(pattern)
            #result+=count_score(pattern)
            pattern=[]
            
        else:
            pattern.append(l)
    
        #print(number_of_valid_combination)
    patterns.append(pattern)
    #pattern=[]
    #result+=count_score(pattern)
total=0
gains=[]                               
for ip,p in enumerate(patterns):
    pass
    result=0
    #Calculate original lines:
    p_mirrors={}
    for i in range(len(p)-1):
        if p[i+1]==p[i]:
            if mirror(p,i+1):
                p_mirrors[ip,0]=i
    p3=transpose(p)
    for i in range(len(p3)-1):
        if p3[i+1]==p3[i]:
            if mirror(p3,i+1):
                p_mirrors[ip,1]=i

    for j in range(len(p)):
        for k in range(len(p[0])):
            p2=copy.deepcopy(p)
            change="1" if p[j][k]=='0' else '0'
            p2[j]=p[j][:k]+change+p[j][k+1:]
            for i in range(len(p2)-1):
                if p2[i+1]==p2[i]:
                    if mirror(p2,i+1):
    
                        if (ip,0) in p_mirrors:
                            if p_mirrors[ip,0]!=i:
                                result+=100*(i+1)
                                gains.append(result)
                                total+=result
                                break
                        else:
                            result+=100*(i+1)
                            gains.append(result)
                            total+=result
                            break
            else:
                #p3=copy.deepcopy(p)
                p3=transpose(p2)
                for i in range(len(p3)-1):
                    if p3[i+1]==p3[i]:
                        if mirror(p3,i+1):
                            if (ip,1) in p_mirrors:
                                if p_mirrors[ip,1]!=i:
                                    result+=i+1
                                    gains.append(result)
                                    total+=result
                                    break
                            else:
                                result+=i+1
                                gains.append(result)
                                total+=result
                                break
                else:
                    continue
            break
        else:
            continue
        break
    else:
        
        continue
    #break
print("result:",total)
#print(gains)
