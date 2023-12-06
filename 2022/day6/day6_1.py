import os

#input1='./day2/sample.txt'
inputFile='input.txt'
sample1='mjqjpqmgbljsphdztnvjfqwrcgsmlb'
sample2='bvwbjplbgvbhsrlpgdmjqwftvncz'
sample3='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
#input=sample3
with open(inputFile) as f:
    #lines = f.readlines()
    lines = f.read().splitlines()
    input=lines[0]
    print(input)
    for i in range(3,len(input)):
        pack=set(input[i-13:i+1])
        if len(pack)==14:
            print(i+1)
            break