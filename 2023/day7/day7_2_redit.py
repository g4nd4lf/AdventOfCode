from collections import Counter
import os
os.chdir("./day7")
lookup,hands,ts="AKQT98765432J"[::-1],[],0
for line in open("input.txt"):
  cards, score=line.split()
  cnt=Counter(cards)
  jokers=cnt.get("J",0)
  cnt["J"]=0
  cnt=sorted(cnt.values(), reverse=True)
  cnt[0]+=jokers
  cardcodes=[lookup.find(ch) for ch in cards]
  hands.append((cnt,cardcodes,int(score)))
#print(sum((i+1)*hand[2] for i, hand in enumerate(sorted(hands))))
for h in sorted(hands):
    print(h)