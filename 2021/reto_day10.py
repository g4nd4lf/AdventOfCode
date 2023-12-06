#f = open("id10pru.txt", "r")
f = open("input_day10.txt", "r")
input=f.read()
ilines=input.splitlines()
totalError=0
for line in ilines:
#for i in range(0,len(ilines)):
    err=0
    k=0
    recuento=[]
    for k in range(len(line)):
        c=line[k]
        if c==")":
            if recuento[-1]=="(":
                recuento.pop(-1)
            else:
                err=3
                break
        elif c=="]":
            if recuento[-1]=="[":
                recuento.pop(-1)
            else:
                err=57
                break
        elif c=="}":
            if recuento[-1]=="{":
                recuento.pop(-1)
            else:
                err=1197
                break
        elif c==">":
            if recuento[-1]=="<":
                recuento.pop(-1)
            else:
                err=25137
                break
        else:
            recuento.append(c)
        k+=1
    totalError+=err
print(totalError)


        
        