#import pandas as pd
import os
os.chdir("./2023/day4")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'
        
with open(input1) as f:
    lines = f.readlines()
    points=0
    for l in lines:
        l=l.replace("\n","")
        winners=set(l.split(":")[1].split(" | ")[0].split())
        my_numbers=set(l.split(":")[1].split(" | ")[1].split())
        #print (winners,"|",my_numbers)
        hits=0
        for n in my_numbers:
            if n in winners:
                hits+=1
        if hits>0:
            points+=2**(hits-1)
        print(points)