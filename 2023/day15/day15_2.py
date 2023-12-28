import os
os.chdir("./day15")
#input1='sample.txt'
input1='input.txt'

def hashmap(command,val):
    res=val
    for c in command:
        res+=ord(c)
        res*=17
        res=res%256
    return res
def dash(boxes,box,label):
    indice_a_eliminar = next((i for i, lens in enumerate(boxes[box]) if lens[0] == label), None)

    # Eliminar el elemento si se encuentra
    if indice_a_eliminar is not None:
        boxes[box].pop(indice_a_eliminar)


def equal(boxes,box,label,value):
    indice_a_actualizar = next((i for i, lens in enumerate(boxes[box]) if lens[0] == label), None)
    if indice_a_actualizar is None:
        boxes[box].append([label,int(value)])
    else:
        boxes[box][indice_a_actualizar][1]=int(value)
    
    boxes[box]
def calc_focusing_power(boxes):
    result=0
    for i,b in enumerate(boxes):
        for j,lens in enumerate(b):
            result+=(i+1)*(j+1)*lens[1]
    return result

boxes = [[] for _ in range(256)]
print("Reading and parsing data:")
result=0
#orig_stones=[]
with open(input1) as f:
    data=f.read()
    commands=data.split(",")
    #commands=["HASH","rn","cm","qp","ot","ab","pc"]
    for c in commands:
        if c[-1]=='-':
            label=c[:-1]
            box=hashmap(label,0)
            dash(boxes,box,label)
        else:
            label,value=c.split("=")
            box=hashmap(label,0)
            equal(boxes,box,label,value)

result=calc_focusing_power(boxes)

print("Result: ", result)