import heapq
import os
from treelib import Node, Tree

os.chdir("./day22")
input1='sample.txt'
#input1='input.txt'
max_steps=40
ids=0
endtracks=0
def neighbourgs(node,tree,xmax,y    max,obstacles,ids):
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pos=node.tag
    isendtrack=True
    for direccion in direcciones:
        neigh = (pos[0] + direccion[0], pos[1] + direccion[1])
        pass
        if neigh not in obstacles and 0 <= neigh[0] < xmax and 0<= neigh[1] < ymax:
            ids=ids+1
            if not [neigh,node.data+1] in [[tree[x].tag,tree[x].data] for x in tree.expand_tree(mode=Tree.DEPTH)]:
                #print("repe: ", neigh)
            #else:
                tree.create_node(neigh,ids,parent=node.identifier,data=node.data+1)
                isendtrack=False

    return tree,ids,isendtrack


obstacles=set()
print("Reading and parsing data:")

with open(input1) as f:
    lines=f.readlines()
    for j,l in enumerate(lines):
        l=l.replace("\n","")
        obstacles.update([(i,j) for i, c in enumerate(l) if c == "#"])
        s_id=l.find("S")
        if s_id>0:
            s=(j,s_id)
print("obstacles: ",obstacles)
print("s: ",s)

xmax=len(lines[0])-1
ymax=len(lines)

garden=Tree()
garden.create_node(s,0,data=1)
leaves=garden.leaves()
left_leaves=[x for x in leaves if x.data<max_steps]
old_leaves=[]
while(len(left_leaves)>0 and left_leaves!=old_leaves):
    for l in left_leaves:
        garden,ids,isendtrack=neighbourgs(l,garden,xmax,ymax,obstacles,ids)
        if isendtrack:
            endtracks+=1
        #for n in new_nodes: 
        #    if n!=l:
        #        garden.create_node(n,n,parent=l,data=l.data+1)
    leaves=garden.leaves()
    old_leaves=left_leaves
    left_leaves=[x for x in leaves if x.data<max_steps]
    pass
print("arbol creado")
visited_gardens=set()
#Recorrer arbol y añadir nodos a visited_gardens
visited_gardens.update((node.tag,node.data) for node in garden.leaves() if node.data==max_steps)
print("RESULT: ",len(visited_gardens))
#print(visited_gardens)

