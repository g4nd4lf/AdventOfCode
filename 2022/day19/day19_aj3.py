
#! /usr/bin/python3
import re
import sys
import numpy
import os,pathlib
currentFileDir=pathlib.Path(__file__).parent.resolve()
os.chdir(currentFileDir)


MINERALS = {'ore': 0, 'clay': 1, 'obsidian': 2, 'geode': 3}
def to_array(blueprint):
    arr = numpy.zeros([4, 4], dtype=numpy.uint32)
    for robot in blueprint:
        i = MINERALS[robot['type']]
        for n, mineral in robot['costs']:
            j = MINERALS[mineral]
            arr[i][j] = n
    return arr


def parse_input(path):
    words = open(path).read().split()
    blueprints = []
    i = 0
    while i < len(words):
        if words[i] == 'Blueprint':
            blueprints.append([])
            i += 2
        elif words[i] == 'Each':
            robot = {'type': words[i + 1], 'costs': []}
            blueprints[-1].append(robot)
            i += 4
        elif words[i] == 'and':
            i += 1
        else:
            assert words[i].isdigit(), (i, words[i])
            quantity = int(words[i])
            mineral = words[i + 1].rstrip('.')
            blueprints[-1][-1]['costs'].append((quantity, mineral))
            i += 2
    return [to_array(blueprint) for blueprint in blueprints]


def prune_states(states, max_costs, time_left):
    states = states.copy()

    # Once we have enough of a reosurce that we can't ever run out, there
    # is no benefit to tracking quantities of the resource above that level,
    # so we cap resource counts to keep state counts down
    for state in states:
        for i in range(3):
            deficit = max_costs[i] - state[i]
            max_useful_quantity = max_costs[i] + deficit * time_left
            if state[i + 4] >= max_useful_quantity:
                state[i + 4] = max_useful_quantity
    #Con lo siguiente ordeno los estados por columnas, 
    for i in range(7, -1, -1):
        idxs = numpy.argsort(states[:, i], kind='stable')
        states = states[idxs]
    #Con esto creo una matriz numpy de 0 con las mismas dimensiones que state
    new_states = numpy.zeros(states.shape, dtype=states.dtype)
    n = 0

    for i in range(len(states)):
        redundant = numpy.any(numpy.all(states[i] <= states[i+1:], axis=1))
        if not redundant:
            new_states[n] = states[i]
            n += 1
        else:
            a="holala"
    print(time_left,len(states))
    return new_states[:n]

allEstates=[]
def simulate(blueprint, duration):
    max_costs = [max(blueprint[i][j] for i in range(4)) for j in range(4)]
    states = numpy.zeros([1, 8], dtype=numpy.uint32)
    states[0][0] = 1

    for i in range(duration):
        new_states = numpy.zeros([0, 8], dtype=numpy.uint32)
        for state in states:
            robots = state[:4]
            resources = state[4:]
            n = len(new_states)
            new_states = numpy.resize(new_states, (n + 1, 8))
            new_states[n] = numpy.append(robots, resources + robots)
            for j, robot_cost in enumerate(blueprint):
                if j < 3 and robots[j] >= max_costs[j]:
                        continue # No benefit to building more robots of this type
                if numpy.all(resources >= robot_cost):
                    new_robots = robots.copy()
                    new_robots[j] += 1
                    new_resources = resources + robots - robot_cost
                    n = len(new_states)
                    new_states = numpy.resize(new_states, (n + 1, 8))
                    new_states[n] = numpy.append(new_robots, new_resources)
        pre_prune = len(new_states)
        states = prune_states(new_states, max_costs, duration - i - 1)
        allEstates.append(states)
        #print(i,len(states))
    return  max(states[:, 7])


def main(input_file):
    blueprints = parse_input(input_file)

    quality = 0
    #n = simulate(blueprints[1], 24)
    #print(n)
    # ns=[]
    # #for i, blueprint in enumerate([blueprints[]]):
    # for i, blueprint in enumerate(blueprints):
    #     n = simulate(blueprint, 24)
    #     ns.append(n)
    #     print(ns)
    #     #print(n)
    #     quality += (i + 1) * n
    # print("Part 1:", quality)
    # print(ns)
    product = 1
    ns2=[]
    for i, blueprint in enumerate(blueprints[1:2]):
        n = simulate(blueprint, 32)
        ns2.append(n)
        product *= n
    print("Part 2:", product)
    print(ns2)

main("input.txt")
# if __name__ == '__main__':
#     main(sys.argv[1])