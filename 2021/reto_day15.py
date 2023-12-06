import pandas as pd
import numpy as np
import time

#f = open("id15pru.txt", "r")
#f = open("input_day15.txt", "r")
f = open("input15_2.txt", "r")
input=f.read()
lines=input.splitlines()

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
lastColum=len(lines[0])-1
lastRow=len(lines)-1
values=[]
for i in range(lastRow+1):
    values.append(list(lines[i]))
    for j in range(lastColum+1):
        vertices.append((i,j))
vals=pd.DataFrame(values).astype(int)
vals2=vals.to_numpy()

g={}
for v in vertices:
    if v!=(lastRow,lastColum):
        if v[0]==lastRow:
            newEdge={(v[0],v[1]+1)}
        elif v[1]==lastColum:
            newEdge={(v[0]+1,v[1])}
        else:
            newEdge={(v[0]+1,v[1]),(v[0],v[1]+1)}
    g[v]=newEdge



            
    
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
path = graph.find_all_paths((0,0), (lastRow,lastColum))
minRisk=10000
#m = np.array(values)
m= vals2
p0=int(vals.iloc[0,0])
start = time.time()
print("Empezamos...")
for p in path:
    #df=vals.iloc[list(p2[0]),list(p2[1])].astype(int)
    #p2=[*zip(*p)]
    listValues = m[tuple(np.transpose(p))].tolist()
    pathRisk=sum(listValues)-p0
    if pathRisk<minRisk:
        minRisk=pathRisk
    #print(pathRisk)
end = time.time()
print(minRisk)
print(end-start)
# for p in path:
#     pathRisk=-int(vals.iloc[0,0])
#     for coor in p:
#         pathRisk+=int(vals.iloc[coor[0],coor[1]])
#     if pathRisk<minRisk:
#         minRisk=pathRisk
#     print(pathRisk)
        
# #print(path)
# print(minRisk)


# def masCorto(x,y):
#     if(x[0]==lastRow-1 and x[1]==lastColum-1):
        