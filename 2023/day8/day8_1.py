import os
from operator import itemgetter

os.chdir("./day8")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'

with open(input1) as f:
    lines=f.readlines()
    print(lines[0])
    commands=lines[0].replace('\n','')
    desertmap={}
    for l in lines[2:]:
      l=l.replace("\n","")
      src=l.split(" = ")[0]
      dst=l.split(" = ")[1]
      dst=tuple(dst[1:-1].split(', '))
      desertmap[src]=dst
    print(desertmap)
    pos='AAA'
    ic=0
    i=0
    while pos!='ZZZ':
        c=commands[ic]
        if c=='L':
            pos=desertmap[pos][0]
        else:
            pos=desertmap[pos][1]
        i+=1
        ic+=1
        if ic==len(commands):
            ic=0
    print(i)


          
#     hands=[]
#     for l in lines:
#         handCards=l.split()[0]
#         handBids=l.split()[1]
#         handType=cardtype(handCards)
#         handValue=calcHandValue(handCards)
#         hands.append((handCards,handBids,handType,handValue))
#     #for h in hands:
#     #    h=h.append(cardtype(h[0]))
#     ordered_hands=sorted(hands, key=itemgetter(2,3))
#     #ordered_hands.reverse()
#     #print(ordered_hands)
#     winnings=0
#     for i,hand in enumerate(ordered_hands):
#         winnings+=(i+1)*int(hand[1])
#         #print(i,int(hand[1]))

# print(winnings)