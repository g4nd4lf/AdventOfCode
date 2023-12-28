# from binarytree import Node 
# root = Node(0) 
# root.left = Node(0) 
# root.right = Node(1) 

# print(root)

from binarytree import build, Node

def obtener_listas_de_ramas(raiz):
    listas_ramas = []
    _obtener_listas_de_ramas(raiz, [], listas_ramas)
    return listas_ramas

def _obtener_listas_de_ramas(nodo, lista_actual, listas_ramas):
    if nodo is None:
        return

    lista_actual.append(nodo.value)

    if nodo.left is None and nodo.right is None:
        listas_ramas.append(list(lista_actual))
    else:
        _obtener_listas_de_ramas(nodo.left, lista_actual, listas_ramas)
        _obtener_listas_de_ramas(nodo.right, lista_actual, listas_ramas)

    lista_actual.pop()

# Generar árbol binario de altura 6
altura = 6
#arbol = build([0,1,1,1,0,None,0,1,1,0,0])
arbol = Node(0)
parent=arbol
for i in range(3):
    parent.left=Node(0)
    parent.right=Node(1)


# Obtener listas de 0 y 1 para cada rama
listas_ramas = obtener_listas_de_ramas(arbol)

# Imprimir resultados
print("Árbol binario:")
print(arbol)
print("\nListas de 0 y 1 para cada rama:")
for lista in listas_ramas:
    print(lista)
