from itertools import cycle
import os,pathlib

currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)

dec_key = 811589153

mixed=[]
def solve(task):
    rounds, mutliply = (1, 1) if task == 1 else (10, dec_key)
    with open("input.txt") as f:
        numbers = [int(n) * mutliply for n in f.readlines()]
    #numbers =[1, 2, -3, 3, -2, 0, 4]
    #numbers=[-16, 2, -3, 3, -2, 0, 4]
    mixed = [a for a in enumerate(numbers)]
    cyc = cycle(mixed.copy())
    zero_tuple = (numbers.index(0), 0)
    lm = len(mixed) - 1

    #for _ in range(rounds * len(numbers)):
    for _ in range(5):
        curr = next(cyc)
        idx_old = mixed.index(curr)
        mixed.remove(curr)
        idx_new = (idx_old + curr[1] + lm) % lm
        mixed.insert(idx_new, curr)

    idx_zero_tuple = mixed.index(zero_tuple)
    print(sum([mixed[(idx_zero_tuple + i) % len(numbers)][1]
          for i in [1000, 2000, 3000]]))
    return(mixed,numbers)

mix,num=solve(task=1)
#solve(task=2)