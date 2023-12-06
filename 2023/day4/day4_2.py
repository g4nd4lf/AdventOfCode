#import pandas as pd
import os
os.chdir("./2023/day4")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'
with open(input1) as f:
    lines = f.readlines()
    cards=[]
    copies=[1]*len(lines)
    points=0
    for i,l in enumerate(lines):
        l=l.replace("\n","")
        winners=set(l.split(":")[1].split(" | ")[0].split())
        my_numbers=set(l.split(":")[1].split(" | ")[1].split())
        hits=0
        for n in my_numbers:
            if n in winners:
                hits+=1
        cards.append(hits)
    numcards=0
    for i in range(len(copies)):
        for j in range(i+1,i+1+cards[i]):
            copies[j]+=copies[i]
    print(sum(copies))
