import numpy as np
import math
import re
import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import time


def height(c):
    p = ord(c)
    if p > 96:
        p = p - 96
    else:
        p = p - 64 + 26
    return p


def adjacent_nodes(node):
    adjacent = [(node[0] + 1, node[1]), (node[0] - 1, node[1]), (node[0], node[1] - 1), (node[0], node[1] + 1)]
    return [x for x in adjacent if (0 <= x[0] < xmax and 0 <= x[1] < ymax)]


if __name__ == '__main__':
    # Getting the input
    # filename = "12.txt"
    # inp = open(filename, "r")
    # # print(f.read()) #f.readline()  f.read(x)
    # inputstring = inp.readlines()
    # inp.close()
    input2 = np.loadtxt("12.txt", dtype=str)
    map_temp = [list(line) for line in input2]
    map = np.array([[height(c) for c in line] for line in input2])
    xmax, ymax = map.shape

    start = np.where(map == height('S'))
    xstart = start[0][0]
    ystart = start[1][0]
    start = (xstart, ystart)

    end = np.where(map == height('E'))
    xend = end[0][0]
    yend = end[1][0]
    end = (xend, yend)

    map[start] = height('a')
    map[end] = height('z')

    #start = (0,0)

    # part 1
    distances_from_start = np.zeros((xmax, ymax), int) + (xmax * ymax)
    distances_from_start[start] = 0

    not_yet_visited = [(x, y) for x in range(xmax) for y in range(ymax)]
    not_yet_visited.remove(start)
    next_to_visit = [start]

    while len(next_to_visit) > 0:
        current_node = next_to_visit.pop(0)
        for next_node in adjacent_nodes(current_node):
            if map[next_node] <= map[current_node] + 1:
                if distances_from_start[next_node] > distances_from_start[current_node] + 1:
                    distances_from_start[next_node] = distances_from_start[current_node] + 1
                    not_yet_visited.remove(next_node)
                    next_to_visit.append(next_node)

    print(distances_from_start[end])

    # part 2
    print('Day12')
    distances_from_end = np.zeros((xmax, ymax), int) + (xmax * ymax)
    distances_from_end[end] = 0

    not_yet_visited = [(x, y) for x in range(xmax) for y in range(ymax)]
    not_yet_visited.remove(end)
    next_to_visit = [end]

    while len(next_to_visit) > 0:
        current_node = next_to_visit.pop(0)
        for next_node in adjacent_nodes(current_node):
            if map[current_node] <= map[next_node] + 1:
                if distances_from_end[next_node] > distances_from_end[current_node] + 1:
                    distances_from_end[next_node] = distances_from_end[current_node] + 1
                    not_yet_visited.remove(next_node)
                    next_to_visit.append(next_node)

    [rows, columns] = np.where(map == 1)

    print(min([distances_from_end[(rows[i], columns[i])] for i in range(len(rows))]))
    minimal_distance = xmax * ymax
    # for i in range(len(rows)):
        # print(distances_from_end[(rows[i], columns[i])])

    print([distances_from_start[s]] for s in np.where(map == 1))
