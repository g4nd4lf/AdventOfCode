import os
import math
import sys
import numpy as np
import pathlib
import heapq
from functools import total_ordering

currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)
#inputFile='input.txt'
inputFile='sample.txt'
@total_ordering
class Node:
    def __init__(self, coor: complex, value: int, parent):
        self.value = value
        self.coor = coor
        self.parent = parent
        self.h = 0
        self.g = 0
        self.f = 0

    def __repr__(self):
        return repr((self.coor, self.value))

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.coor == other.coor
        elif isinstance(other, complex):
            return self.coor == other
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Node):
            return (self.coor.real < other.coor.real) and (self.coor.imag < other.coor.imag)
        elif isinstance(other, complex):
            return (self.coor.real < other.real) and (self.coor.imag < other.imag)
        else:
            return False

    def __hash__(self):
        return hash(self.coor)

    def add(self, other, value):
        return Node(complex(self.coor.real + other.real, self.coor.imag + other.imag), value, self)

def in_bounds(hmap, location: complex, x_max: int, y_max: int) -> bool:
    return (0 <= location.real < x_max) and (0 <= location.imag < y_max)

def dijkstra(hmap: dict, start: complex, end: complex):
    distance = {k: sys.maxsize for k in hmap}
    distance[start] = 0
    previous = {k: None for k in hmap}
    visited = set()
    queue = []
    vecs = (0 - 1j, -1 + 0j, 1 + 0j, 0 + 1j)
    x_max, y_max = int(max(k.real for k in hmap)) + 1, int(max(k.imag for k in hmap)) + 1
    start_node = Node(start, hmap[start], None)
    heapq.heappush(queue, (distance[start], start_node))
    while queue:
        _, current = heapq.heappop(queue)
        visited.add(current)
        if current.coor == end:
            break
        neighbors = [current.add(vec, hmap[current.coor + vec]) for vec in vecs if in_bounds(hmap,
                                                                                             current.coor + vec,
                                                                                             x_max,
                                                                                             y_max)]
        validNeighbors=[n for n in neighbors if n.value-current.value<=1]                                                                                             
        for neighbor in validNeighbors:
            if neighbor not in visited:
                neighbor.f = current.f + 1 #hmap[neighbor.coor]
                if neighbor.f < distance[neighbor.coor]:
                    distance[neighbor.coor] = neighbor.f
                    previous[neighbor.coor] = current.coor
                    heapq.heappush(queue, (distance[neighbor.coor], neighbor))
    return distance[end]

def read_and_init(fn):
    with open(fn, 'r') as fo:
        lines = fo.read().splitlines()
    hmap = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            step=lines[y][x]
            if step=='S':
                s=x+1j*y
                step="a"
            elif lines[y][x]=='E':
                e=x+1j*y
                step="z"
            hmap[x + 1j * y] = ord(step)-ord('a')
    return hmap,s,e

hmap,s,e = read_and_init('input.txt')
min_dist = dijkstra(hmap,s,e)
print('Part 1:', min_dist)
