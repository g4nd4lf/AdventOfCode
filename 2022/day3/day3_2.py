import os

#input1='./day3/sample.txt'
input1='input.txt'
#input1='sample.txt'

print(os.getcwd())
i1=ord('a')-1
i2=ord('A')-27
sum=0
priority=0
with open(input1) as f:
    #lines = f.readlines()
    lines = f.read().splitlines()
    for i in range(0,len(lines),3):
        s1=set(lines[i])
        s2=set(lines[i+1])
        s3=set(lines[i+2])
        c=s1.intersection(s2).intersection(s3).pop()
        #print(c)
        if ord(c)>96: #minuscula
            priority=ord(c)-i1
        else:
            priority=ord(c)-i2
        #print(priority)
        sum+=priority
print(sum)

    # for l in lines:
    #     s1=set(l[0:(len(l)//2)])
    #     s2=set(l[len(l)//2:])
    #     c=s1.intersection(s2).pop()
    #     if ord(c)>96: #minuscula
    #         priority=ord(c)-i1
    #     else:
    #         priority=ord(c)-i2
    #     print(priority)
    #     sum+=priority
#print(sum)