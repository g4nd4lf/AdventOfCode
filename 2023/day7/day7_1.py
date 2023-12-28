import os
from operator import itemgetter

os.chdir("./day7")
print(os.getcwd())
#input1='sample.txt'
input1='input.txt'

cards=("2","3","4","5","6","7","8","9","T","J","Q","K","A")

def count(hand):
    counts={}
    for c in hand:
        counts[c]=hand.count(c)
    return counts
def cardtype(hand):
    handcounts=count(hand)
    handcount=handcounts.values()
    if any(c==5 for c in handcount):
        return 7
    if any(c==4 for c in handcount):
        return 6
    if any(c==3 for c in handcount):
        if any(c==2 for c in handcount):
            return 5
        else:
            return 4
    pairs=sum(c==2 for c in handcount)
    if pairs==2:
        return 3
    if pairs==1:
        return 2
    return 1

def calcHandValue(handCards):
    value=0
    for i,h in enumerate(handCards):
        value+=cards.index(h)*13**(len(handCards)-i)
    return value

with open(input1) as f:
    lines=f.readlines()
    hands=[]
    for l in lines:
        handCards=l.split()[0]
        handBids=l.split()[1]
        handType=cardtype(handCards)
        handValue=calcHandValue(handCards)
        hands.append((handCards,handBids,handType,handValue))
    #for h in hands:
    #    h=h.append(cardtype(h[0]))
    ordered_hands=sorted(hands, key=itemgetter(2,3))
    #ordered_hands.reverse()
    #print(ordered_hands)
    winnings=0
    for i,hand in enumerate(ordered_hands):
        winnings+=(i+1)*int(hand[1])
        #print(i,int(hand[1]))

print(winnings)