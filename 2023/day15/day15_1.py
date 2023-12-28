import os
os.chdir("./day15")
#input1='sample.txt'
input1='input.txt'

def calculate(command,val):
    res=val
    for c in command:
        res+=ord(c)
        res*=17
        res=res%256
    return res
        


print("Reading and parsing data:")
result=0
#orig_stones=[]
with open(input1) as f:
    data=f.read()
    commands=data.split(",")
    #commands="HASH"
    for c in commands:
        result+=calculate(c,0)

print("Result: ", result)