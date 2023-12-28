import os

os.chdir("./day7")

deck = 'AKQJT98765432'
deck_ = 'AKQT98765432'
cards = {v:str(i+1).zfill(2) for (i,v) in enumerate(deck[::-1])} 
cards_ = {v:str(i+1).zfill(2) for (i,v) in enumerate(deck[::-1])}
cards_['J'] = '00'
rank = [] 
rank_ = []

with open('sample.txt') as input: 
    for line in input: hand, bid = line.replace('\n', '').split(' ')
    typ = ''.join(sorted([str(hand.count(i)) if hand.count(i) > 0 else '' for i in deck])).zfill(5)[::-1]
    value = ''.join(map(lambda x: cards[x], hand))
    
    poss = []
    for d in deck_:
        hand_ = hand.replace('J', d)
        poss.append((''.join(sorted([str(hand_.count(i)) if hand_.count(i) > 0 else '' for i in deck])).zfill(5)[::-1], hand_))
    
    typ_, hand_ = max(poss)
    value_ = ''.join(map(lambda x: cards_[x], hand))
    
    rank.append((typ+value, int(bid)))
    rank_.append((typ_+value_, int(bid)))

#print(sum([(i+1)*v for (i,(,v)) in enumerate(sorted(rank))]))
print(sorted(rank_))