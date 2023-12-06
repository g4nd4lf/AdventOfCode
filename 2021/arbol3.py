from anytree import Node, RenderTree, PreOrderIter, findall_by_attr, Walker


def findpaths(self):
    if not self.children:
        return [[self.name]]  # one path: only contains self.value
    paths = []
    for child in self.children:
        for path in findpaths(child):
            paths.append([self.name] + path)
    return paths

udo = Node({"Udo",4})
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)

arbol=Node([0,0])
for i in range(3):
    rama=Node([i,i],parent=arbol)
    for j in range(4):
        hijo=Node([i,j],parent=rama)
    #arboles.append(arbol)

#print(udo)
Node('/Udo')
#print(joe)
Node('/Udo/Dan/Joe')

for pre, fill, node in RenderTree(udo):
    print("%s%s" % (pre, node.name))

#print(dan.children)
#(Node('/Udo/Dan/Jet'), Node('/Udo/Dan/Jan'), Node('/Udo/Dan/Joe'))

# for node in PreOrderIter(udo):
#     if len(node.children)==0:
#         print(node.name)
#print([node.name for node in PreOrderIter(udo)])
findall_by_attr(udo, "Jan")
findpaths(dan)
w=Walker()
w.walk(marc,dan)