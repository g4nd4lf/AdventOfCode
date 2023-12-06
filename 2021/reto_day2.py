import pandas as pd
input=pd.read_csv("input_day2.txt",header=None,sep=' ')
input.columns=["com","value"]

#PART 1

position=0
depth=0
for i in range(0,len(input)):
    if (input['com'][i]=='forward'):
        position=position+input['value'][i]
    if (input['com'][i]=='up'):
        depth=depth-input['value'][i]
    if (input['com'][i]=='down'):
        depth=depth+input['value'][i]
print("position: ")
print(position)
print("position: ")
print(depth)
print("position x depth: ")
print(position*depth)

#PART 2

position=0
depth=0
aim=0
for i in range(0,len(input)):
    if (input['com'][i]=='forward'):
        position=position+input['value'][i]
        depth=depth+aim*input['value'][i]
    if (input['com'][i]=='up'):
        aim=aim-input['value'][i]
    if (input['com'][i]=='down'):
        aim=aim+input['value'][i]
print("position: ")
print(position)
print("position: ")
print(depth)
print("position x depth: ")
print(position*depth)