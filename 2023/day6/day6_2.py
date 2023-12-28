import os, math
os.chdir("./day6")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'


with open(input1) as f:
    lines=f.readlines()
    trecord=int(''.join(lines[0].split(":")[1].split()))
    drecord=int(''.join(lines[1].split(":")[1].split()))
    # d>drecord
    # v*(trecord-ton) > drecord
    # ton*(trecord-ton)>drecord
    # -1*ton^2+trecord*ton-drecord>0
    # ton^2-trecord*ton+drecord=0
    # trecord+-sqr(trecord^2-(4*1*drecord))/2

    sol1=abs(math.floor((trecord-(trecord**2-4*drecord)**0.5)/2))+1
    sol2=abs(math.floor((trecord+(trecord**2-4*drecord)**0.5)/2))
    print(trecord,drecord)
    print(sol1,sol2)
    print(sol2-sol1+1)
    #v=13
    #d=v*(trecord-v)
    #print(d,drecord)
    # options=[]
    # total=1
    # for i,tr in enumerate(trecords):
    #     newoptions=[]
    #     for ton in range(tr):
    #         v=ton
    #         d=v*(tr-ton)
    #         if d>drecords[i]:
    #             newoptions.append(ton)
    #     total*=len(newoptions)
    #     options.append(newoptions)
    # print(options)
    # print(total)

