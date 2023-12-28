import os
os.chdir("./day6")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'


with open(input1) as f:
    lines=f.readlines()
    trecords=[int(x) for x in lines[0].split(":")[1].split()]
    drecords=[int(x) for x in lines[1].split(":")[1].split()]
    options=[]
    total=1
    for i,tr in enumerate(trecords):
        newoptions=[]
        for ton in range(tr):
            v=ton
            d=v*(tr-ton)
            if d>drecords[i]:
                newoptions.append(ton)
        total*=len(newoptions)
        options.append(newoptions)
    print(options)
    print(total)

#     for r in rest:
#         strings=r.split("\n")[1:]
#         newmap=[]
#         for s in strings:
#             newmap.append([int(x) for x in s.split()])
#         maps.append(newmap)
#     print(maps)
# locations=[]
# for s in seeds:
#     res=s
#     for m in maps:
#         s=map(s,m)
#     locations.append(s)
# print(locations,min(locations))