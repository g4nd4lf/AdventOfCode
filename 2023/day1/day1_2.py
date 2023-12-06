#import pandas as pd
import os,sys
print(sys.version)
os.chdir("./2023/day1")
print(os.getcwd())
#   digitletters=["one","two","three","four", "five":5, "six":6, "seven":7, "eight":8, "nine"]
digitletters={"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
#input1='sample4.txt'
input1='input.txt'
def find_first_number(str):
    positions=[]
    for d in digitletters:
        position=str.find(d)
        if position != -1:
            positions.append((d,position))
    if len(positions)>0:
        ordered_positions=sorted(positions, key=lambda x: x[1])
        return(ordered_positions[0])
    else:
        return(-1)
def find_last_number(str):
    positions=[]
    for d in digitletters:
        newposition=str.find(d)
        position=-1
        while newposition != -1:
            position=newposition
            newposition=str.find(d,position+1)
        if position != -1:
            positions.append((d,position))
    ordered_positions=sorted(positions, key=lambda x: x[1])
    if len(ordered_positions)>0:
        return(ordered_positions[-1])
    else: return(-1)
with open(input1) as f:
    suma=0
    lines = f.readlines()
    for l in lines:
        first_number=find_first_number(l)
        last_number=find_last_number(l)
        if first_number!=-1:
            l=l[:first_number[1]]+str(digitletters[first_number[0]])+l[first_number[1]+1:]
            #l=l.replace(first_number[0],str(digitletters[first_number[0]]))
            l=l.replace(last_number[0],str(digitletters[last_number[0]]))
    
        digits=""
        for c in l:
            if c.isdigit():
                digits+=c
        #if len(digits)>1:
        calibration=digits[0]+digits[-1]
        #elif len(digits)>0:
        #    calibration=digits[0]
        #else:
        #    calibration=0
        print(calibration)
        suma+=int(calibration)
        #break
    print(suma)