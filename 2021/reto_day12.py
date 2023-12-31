#f = open("id12pru3.txt", "r")
f = open("input_day12.txt", "r")
input=f.read()
ilinesS=input.splitlines()

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        """ returns a list of all the edges of a vertice"""
        return self._graph_dict[vertice]
        
    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        return set(self._graph_dict.keys())

    def all_edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    
    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex 
            in graph """
        if path == None:
            path = []
        graph = self._graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, 
                                               end_vertex, 
                                               path)
                if extended_path: 
                    return extended_path
        return None

    def singleSmall(self,vertex,path=[]):
        if vertex.isupper():
            return True
        elif (vertex=='start' or vertex=='end'):
            return False
        else:
            minusc=[x for x in path if x.islower()]
            return not (len(minusc))!=len(set(minusc))
    
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        
        graph = self._graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if (vertex not in path) or (self.singleSmall(vertex,path)):
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                for p in extended_paths: 
                    paths.append(p)
        return paths
vertices=[]
for i in ilinesS:
    v0=i.split("-")[0]
    if v0 not in vertices:
        vertices.append(v0)
    v1=i.split("-")[1]
    if v1 not in vertices:
        vertices.append(v1)
g={}
for v in vertices:
    for i in ilinesS:
        vs=i.split("-")    
        for v in vs:
            newEdge= vs[0] if vs[1]==v else vs[1]
            if v in g:
                if newEdge not in g[v]:
                    g[v].add(newEdge)
            else:
                g[v]={newEdge}
            

            
    
# g = { "a" : {"d", "f"},
#       "b" : {"c"},
#       "c" : {"b", "c", "d", "e"},
#       "d" : {"a", "c", "f"},
#       "e" : {"c"},
#       "f" : {"a", "d"}
#     }


graph = Graph(g)
print("Vertices of graph:")
#print(graph.all_vertices())

print("Edges of graph:")
#print(graph.all_edges())


print('All paths from vertex "a" to vertex "b":')
path = graph.find_all_paths("start", "end")
#print(path)
print(len(path))
