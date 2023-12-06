#import pandas as pd
import os
os.chdir("./2023/day1")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'
with open(input1) as f:
    suma=0
    lines = f.readlines()
    for l in lines:
        digits=""
        for c in l:
            if c.isdigit():
                digits+=c
        calibration=digits[0]+digits[-1]
        print(calibration)
        suma+=int(calibration)
    print(suma)