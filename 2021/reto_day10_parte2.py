#f = open("id10pru.txt", "r")
f = open("input_day10.txt", "r")
input=f.read()
ilines=input.splitlines()
totalError=0
totals=[]
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
                break
        elif c=="]":
            if recuento[-1]=="[":
                recuento.pop(-1)
            else:
                break
        elif c=="}":
            if recuento[-1]=="{":
                recuento.pop(-1)
            else:
                break
        elif c==">":
            if recuento[-1]=="<":
                recuento.pop(-1)
            else:
                break
        else:
            recuento.append(c)
        k+=1
        if k==len(line):
            total=0
            for j in range(len(recuento)-1,-1,-1):
                c=recuento[j]
                total=total*5
                if c=='(':
                    total+=1
                elif c=='[':
                    total+=2
                elif c=='{':
                    total+=3
                elif c=='<':
                    total+=4
            print('Total: ',end='')
            print(total)
            totals.append(total)
print("Middle score: ",end='')
print(sorted(totals)[int((len(totals)-1)/2)])

        
        