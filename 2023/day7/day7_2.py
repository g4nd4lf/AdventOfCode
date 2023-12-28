import os
from operator import itemgetter

os.chdir("./day7")
print(os.getcwd())
#input1='sample2.txt'
input1='input.txt'

cards=("J","2","3","4","5","6","7","8","9","T","Q","K","A")

def count(hand):
    counts={}
    numberOfJokes=hand.count('J')
    for c in hand:
        if c!='J':
            counts[c]=hand.count(c)#+numberOfJokes
    return counts
def cardtype(hand):
    handcounts=count(hand)
    numberOfJokes=hand.count('J')
    handcount=handcounts.values()
        
    if any(c+numberOfJokes==5 for c in handcount) or hand=='JJJJJ':
        return 7
    if any(c+numberOfJokes==4 for c in handcount):
        return 6
    #ordered_handcounts=sorted(handcounts,key=handcounts.get,reverse=True)
    if any(c==3 for c in handcount):
        if any(c==2 for c in handcount):
            return 5
    pairs=sum(c==2 for c in handcount)
    if pairs==2 and numberOfJokes==1:    
        return 5
    if any(c+numberOfJokes==3 for c in handcount):        
        return 4
    #if any(c+numberOfJokes==2 for c in handcount):
    if pairs==2 or (pairs==1 and numberOfJokes==1):
        return 3
    if pairs==1 or numberOfJokes==1:
        return 2
    return 1

def calcHandValue(handCards):
    value=0
    for i,h in enumerate(handCards):
        value+=(cards.index(h)+1)*100**(len(handCards)-i)
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
        print(hand)
        #print(i,int(hand[1]))

print(winnings)