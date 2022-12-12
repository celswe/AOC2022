import numpy as np
import math
import re
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import time

def add_to_visited(vis, t):
    visited.add((t[0], t[1]))


def head_take_step(h, d):
    if d == 'U':
        h[1] += 1
    elif d == 'D':
        h[1] += -1
    elif d == 'L':
        h[0] += -1
    elif d == 'R':
        h[0] += 1


def hamming_distance(h, t):
    return max(abs(h[0] - t[0]), abs(h[1] - t[1]))


def min_abs_distance(h, t):
    return min(abs(h[0] - t[0]), abs(h[1] - t[1]))

def visualize(rope):
    return 0

def tail_take_step(h, t, d):
    if hamming_distance(h, t) > 1:
        if h[0] == t[0]:
            dx = 0
            dy = int((h[1] - t[1]) / abs(h[1] - t[1]))
        elif h[1] == t[1]:
            dx = int((h[0] - t[0]) / abs(h[0] - t[0]))
            dy = 0
        else:
            # tail takes diagonal step
            dx = int((h[0] - t[0]) / abs(h[0] - t[0]))
            dy = int((h[1] - t[1]) / abs(h[1] - t[1]))
        t[0] += dx
        t[1] += dy


if __name__ == '__main__':
    # Getting the input
    inp = open("9t.txt", "r")
    # print(f.read()) #f.readline()  f.read(x)
    inputstring = inp.readlines()
    inp.close()

    # head = [0, 0]
    # tail = [0, 0]
    knots = [[0,0] for i in range(10)]
    visited = set()
    add_to_visited(visited, knots[9])

    fig, ax = plt.subplots()
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)

    # Reading in the data
    for line in inputstring:
        line = line.strip()
        print(line)
        # find direction and number of steps
        [(direction, nsteps)] = re.findall('([L, R, U, D]) ([0-9]+)', line)

        # take this number of steps
        for i in range(int(nsteps)):
            head_take_step(knots[0], direction)
            for k in range(1, 10):
                tail_take_step(knots[k-1], knots[k], direction)
            add_to_visited(visited, knots[9])

            ax.cla()
            ax.set_xlim(-20, 20)
            ax.set_ylim(-20, 20)
            ax.plot([k[0] for k in knots], [k[1] for k in knots], 'ro')
            plt.pause(.5)
            print(knots, direction)

    print(len(visited))
    print('Day9')
