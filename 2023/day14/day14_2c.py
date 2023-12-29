# prompt: https://adventofcode.com/2023/day/14

from typing import Callable, cast
import os

os.chdir("./day14")
#input1='sample.txt'
input1='input.txt'

GridPoint = tuple[int, int]
Grid = dict[GridPoint, str]

Points = set[GridPoint]
RangeGen = Callable[[int], range]

def parse_grid(raw_grid: list[str], ignore_chars: str = "") -> Grid:
    """
    returns 2-tuples of (row, col) with their value

    (0, 0) ------> (0, 9)
      |              |
      |              |
      |              |
      |              |
      |              V
    (9, 0) ------> (9, 9)
    """
    result = {}
    ignore = set(ignore_chars)

    for row, line in enumerate(raw_grid):
        for col, c in enumerate(line):
            if c in ignore:
                continue
            result[row, col] = c

    return result

def _roll(
    rocks: Points,
    walls: Points,
    reverse_sort: bool,
    range_builder: RangeGen,
    index_to_replace: int,
):
    for rock in sorted(rocks, reverse=reverse_sort):
        new_rock = None

        for potential_new_value in range_builder(rock[index_to_replace]):
            _new_rock = list(rock)
            _new_rock[index_to_replace] = potential_new_value
            potential_new_rock = tuple(_new_rock)

            if potential_new_rock in walls or potential_new_rock in rocks:
                break
            new_rock = potential_new_rock

        if new_rock is not None:
            rocks.remove(rock)
            rocks.add(cast(GridPoint, new_rock))

def roll_down(rocks, walls, height):
    for row, col in sorted(rocks, reverse=True):
        new_row = None

        for potential_new_row in range(row +1, height):
            potential_new_spot = potential_new_row, col
            if potential_new_spot in walls or potential_new_spot in rocks:
                break
            new_row = potential_new_row

        if new_row is not None:
            rocks.remove((row, col))
            rocks.add((new_row, col))

def roll_left(rocks, walls):
    for row, col in sorted(rocks,key=lambda loc: loc[1]): #ordeno por columnas en vez de filas
        new_col = None

        for potential_new_col in range(col - 1, -1, -1):
            potential_new_spot = row, potential_new_col
            if potential_new_spot in walls or potential_new_spot in rocks:
                break
            new_col = potential_new_col

        if new_col is not None:
            rocks.remove((row, col))
            rocks.add((row, new_col))    

def roll_right(rocks, walls, width):
   for row, col in sorted(rocks,key=lambda loc: loc[1],reverse=True): #ordeno por columnas en vez de filas
        new_col = None

        for potential_new_col in range(col + 1, width):
            potential_new_spot = row, potential_new_col
            if potential_new_spot in walls or potential_new_spot in rocks:
                break
            new_col = potential_new_col

        if new_col is not None:
            rocks.remove((row, col))
            rocks.add((row, new_col))  

def roll_up(rocks,walls):
    for row, col in sorted(rocks):
        new_row = None

        for potential_new_row in range(row - 1, -1, -1):
            potential_new_spot = potential_new_row, col
            if potential_new_spot in walls or potential_new_spot in rocks:
                break
            new_row = potential_new_row

        if new_row is not None:
            rocks.remove((row, col))
            rocks.add((new_row, col))

def part_1(rocks,walls,height):
    roll_up(rocks, walls)
    return sum(height - row for row, _ in rocks)

rocks=set()
walls=set()
with open(input1) as f:
    lines=f.readlines()
    for j,l in enumerate(lines):
        for i,c in enumerate(l):
            if c=='O':
                rocks.add((j,i))
            if c=='#':
                walls.add((j,i))
res=part_1(rocks,walls,len(lines))

print("RESULT: ", res)


def part_2(rocks,walls,height,width):
    NUM_CYCLES = 1_000_000_000

    states={}
    i = 0
    while i < NUM_CYCLES:
        roll_up(rocks, walls)
        roll_left(rocks, walls)
        roll_down(rocks, walls, height)
        roll_right(rocks, walls, width)

        state = frozenset(rocks) #Tras cada ciclo up,left,down,right genero un diccionario con el estado de las rocas

        if state in states and i < 500:    #Si antes de 500 iteracciones encuentro que el nuevo diccionario ya existe en el diccionario de diccionarios states, es que se repite el ciclo
            distance_to_goal = NUM_CYCLES - i  #Esto es el numero de iteracciones para llegar al final
            loop_length = i - states[state]   #Esto es el numero de iteracciones que tarda en repetirse el ciclo
            i = NUM_CYCLES - distance_to_goal % loop_length #si p.ej el numero de ciclos se 20, y quedan 16 para llegar al final y el ciclo se repite cada 3 veces
                                                            #i=20-16%3 = 20-1=19...porque estaba en i=4...7...10...13...16...19 son puntos en que coincide el estado ya calculado, 
                                                            #así que solo tenemos que continuar desde el estado 19

        states[state] = i   #al final almaceno en el diccionaro states el nuevo diccionaro de rocas resultantes state
        i += 1

    return sum(height - row for row, _ in rocks)

res2=part_2(rocks,walls,len(lines),len(lines[0])-1)

print("RESULT2: ", res2)
