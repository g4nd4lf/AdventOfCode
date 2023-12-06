class Arbol:
    def __init__(self, elemento):
        self.hijos = []
        self.elemento = elemento
    def get_leaf_nodes(self):
        leafs = []
        def _get_leaf_nodes( node):
            if node is not None:
                if len(node.hijos) == 0:
                    leafs.append(node)
                for n in node.hijos:
                    _get_leaf_nodes(n)
        _get_leaf_nodes(self.root)
        return leafs

def agregarElemento(arbol, elemento, elementoPadre):
    subarbol = buscarSubarbol(arbol, elementoPadre)
    subarbol.hijos.append(Arbol(elemento))
def buscarSubarbol(arbol, elemento):
    if arbol.elemento == elemento:
        return arbol
    for subarbol in arbol.hijos:
        arbolBuscado = buscarSubarbol(subarbol, elemento)
        if (arbolBuscado != None):
            return arbolBuscado
    return None 
def profundidad(arbol):
    if len(arbol.hijos) == 0: 
        return 1
    return 1 + max(map(profundidad,arbol.hijos)) 
def grado(arbol):
    return max(map(grado, arbol.hijos) + [len(arbol.hijos)])

def get_leaf_nodes(self):
    leafs = []
    def _get_leaf_nodes( node):
        if node is not None:
            if len(node.hijos) == 0:
                leafs.append(node)
            for n in node.hijos:
                _get_leaf_nodes(n)
    _get_leaf_nodes(self.elemento)
    return leafs

abuela = "Jacqueline Gurney"
marge = "Marge Bouvier"
patty = "Patty Bouvier"
selma = "Selma Bouvier"
bart = "Bart Simpson"
lisa = "Lisa Simpson"
maggie = "Maggie Simpson"
ling = "Ling Bouvier"
arbol = Arbol(abuela)
agregarElemento(arbol, patty, abuela)
agregarElemento(arbol, selma, abuela)
agregarElemento(arbol, ling, selma)
agregarElemento(arbol, marge, abuela)
agregarElemento(arbol, bart, marge)
agregarElemento(arbol, lisa, marge)
agregarElemento(arbol, maggie, marge)

print(arbol.get_leaf_nodes())

