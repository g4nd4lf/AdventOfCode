import os
from functools import cache

os.chdir("./day12")
#input1='sample.txt'
input1='input.txt'

@cache
def num_valid_solutions(data,code):
    if len(data)==0:
        return len(code)==0
    if len(code)==0:
        return '#' not in data
    char = data[0]
    if char == ".":
        return num_valid_solutions(data[1:], code)
    if char == "#":
        code0 = code[0]
        # the string is not a possible solution if
        if (len(data)<code0
            or
            any(c=='.' for c in data[:code0])
            or
            #if the string is longer, the char at position code0 can not be '#' because im that case the group of continous # only can be, necessarily of length < code0 or > code0 
            len(data) > code0 and data[code0] == "#" 
            ):
            return 0
        else:
            return num_valid_solutions(data[code0 + 1 :], code[1:])
    if char == '?':
        return num_valid_solutions('#'+data[1:],code)+num_valid_solutions('.'+data[1:],code)


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
        num=num_valid_solutions(data,tuple(code))
        total+=num
    print("total:",total)
