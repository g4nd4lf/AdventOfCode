import os
import math
import numpy as np
import pathlib
import functools

currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)

inputFile='input.txt'
#inputFile='sample.txt'

def compare(v1,v2):
    if isinstance(v1, int) and isinstance(v2, int):
        if v1<v2:
            return 1
        elif v2>v1:
            return -1
        else:
            ret=0
    elif isinstance(v1, list) and isinstance(v2, list):
        if len(v1)==0 and len(v2)>=0:
            return 1
        elif len(v1)>0 and len(v2)==0:
            return -1
        else:
            for i in range(len(v1)):
                if i>len(v2)-1:
                    return -1
                if isinstance(v1[i], int) and isinstance(v2[i], int):
                    if (v1[i]<v2[i]):
                        return 1
                    elif (v1[i]>v2[i]):
                        return -1
                    else:
                        ret=0
                elif isinstance(v1[i], int):
                    ret=compare([v1[i]],v2[i])
                elif isinstance(v2[i], int):
                    ret=compare(v1[i],[v2[i]])                    
                elif len(v1[i])==0 and len(v2[i])>0:
                    return 1
                elif len(v1[i])>0 and len(v2[i])==0:
                    return -1
                elif len(v1[i])==0 and len(v2[i])==0:
                    ret=0
                else:
                    ret=compare(v1[i],v2[i])
                if ret == 1:
                    return 1
                elif ret== -1:
                    return -1
                else:
                    pass
                    # if not compare(v1[i],v2[i]):
                    #     return False
                    # else:
                    #     pass
                    # #return(compare(v1[i],v2[i]))
            return ret
    
#Read input
with open(inputFile) as f:
    lines=f.readlines()
    lines2=list(filter(('\n').__ne__, lines)) #remove empty lines
    packets=[x.replace('\n','') for x in lines2]
    packets+=['[[2]]','[[6]]']
    packs=[eval(x) for x in packets]
    sorted_packs = sorted(packs, key=functools.cmp_to_key(compare),reverse=True)
    print((sorted_packs.index([[2]])+1)*(sorted_packs.index([[6]])+1))
    #data = f.read()
    #pairs=data.split("\n\n")
    #for p in sorted_packs:
    #    print(p)
        # if i==8:
        #     print(p)
        # v=[eval(x) for x in p.split("\n")]
        # if compare(v[0],v[1])==1:
        #     print(i)
        #     sum+=i
        # i+=1
    
    #print("part 1:",sum)
    #.splitlines()