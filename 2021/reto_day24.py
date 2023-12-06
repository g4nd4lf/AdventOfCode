import re
import time
#f = open("id24pru3.txt", "r")
f = open("input_day24.txt", "r")
#model="13579246899999"
input=f.read()
lines=input.splitlines()
d=0
dic=dict()

goodCode=False
#model=99999999999999
model=91411143611081
myTimes=[0]*len(lines)
while goodCode ==False:
    dic["w"]=0
    dic["x"]=0
    dic["y"]=0
    dic["z"]=0
    i=0
    ronda=0
    start = time.time()
    mytimes=[0]*len(lines)
    error=False
    j=0
    k=0
    traman=0
    for line in lines:        
        l=line.split(" ")
        comando=l[0]
        if comando=="inp":
            dic[l[1]]=int(str(model)[i])
            i+=1
        elif comando=="mul":
            if l[2].isnumeric() or l[2].startswith("-"):
                aux=dic[l[1]]*int(l[2])
            else:
                aux=dic[l[1]]*dic[l[2]]
            dic[l[1]]=aux
        elif comando=="eql":
            if l[2].isnumeric() or l[2].startswith("-"):
                m2=int(l[2])
            else:
                m2=dic[l[2]]
            if dic[l[1]]==m2:
                dic[l[1]]=1
            else:
                dic[l[1]]=0
        elif comando=="add":
            if l[2].isnumeric() or l[2].startswith("-"):
                a2=int(l[2])
            else:
                a2=dic[l[2]]
            dic[l[1]]+=a2
        elif comando=="mod":
            if l[2].startswith("-") or dic[l[1]]<0:
                #print("error!")
                error=True
                dic["z"]=1
                break
            elif l[2].isnumeric():
                d2=int(l[2])
            else:
                d2=dic[l[2]]
            dic[l[1]]=dic[l[1]]%d2
        elif comando=="div":
            if l[2].isnumeric() or l[2].startswith("-"):
                d2=int(l[2])
            else:
                d2=dic[l[2]]
            if d2==0:
                #print("error div by 0!")
                error=True
                dic["z"]=1
                break
            dic[l[1]]=int(dic[l[1]]/d2)
        mytimes[i-1]+=time.time()-start
        j+=1
        if k==18:
            k=0
            traman+=1
        else:
            k+=1
    if (dic["z"]==0):
        goodCode=True
        print(str(model))
    else:
        model-=1
        # id=str(model).find("0") #Si encuentro un 0 me salto ese modelo,restando uno mas
        # if id>=0:
        #     model-=1
        # #model=model[:id-1]+str(int(model[id-1])+1)+model[id:] #añado un digito al numero anterior
        # #reemplazo todos los 0 por 1:
        # #model=model.replace("0","1")
        # #ids=[m.start() for m in re.finditer('0', model)]
        # modelS=str(model)
    # if model<99999999991111:
    #     break
    goodCode=True
print(dic)