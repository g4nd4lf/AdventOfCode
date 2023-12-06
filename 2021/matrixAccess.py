a=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19]]
coor=[(0,1),(3,4),(1,2)]
myList=[]
for i in range(len(coor)):
    myList.append(a[coor[i][0]][coor[i][1]])
print(myList)