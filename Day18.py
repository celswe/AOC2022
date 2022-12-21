import numpy as np
import math
import re
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import importlib
from itertools import chain, combinations


def convex_points_between(a, b):
    convex_set = []
    if a[0] == b[0] and a[1] == b[1]:
        convex_set = [(a[0], a[1], i) for i in range(min(a[2], b[2]), max(a[2], b[2]) + 1)]
    elif a[0] == b[0] and a[2] == b[2]:
        convex_set = [(a[0], i, a[2]) for i in range(min(a[1], b[1]), max(a[1], b[1]) + 1)]
    elif a[1] == b[1] and a[2] == b[2]:
        convex_set = [(i, a[1], a[2]) for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1)]
    else:
        convex_set = [a, b]
    return convex_set


def overlap(a, b):
    if a[0] == b[0] and a[1] == b[1] and abs(a[2] - b[2]) == 1:
        return True
    elif a[0] == b[0] and a[2] == b[2] and abs(a[1] - b[1]) == 1:
        return True
    elif a[1] == b[1] and a[2] == b[2] and abs(a[0] - b[0]) == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    # Getting the input
    filename = "18.txt"
    inp = open(filename, "r")
    # print(f.read()) #f.readline()  f.read(x)
    inputstring = inp.readlines()
    inp.close()

    cubes = []
    total_overlap = 0

    for line in inputstring:
        line = line.strip()
        [x, y, z] = re.findall('([0-9]+)', line)
        current_c = (int(x), int(y), int(z))

        for c in cubes:
            if overlap(c, current_c):
                total_overlap += 1

        cubes.append(current_c)

    print('overlap:', total_overlap)
    print('surface:', 6 * len(inputstring) - 2 * total_overlap)

    # part 2
    new_cubes = set()
    # adding the convex hull
    for c in cubes:
        for d in cubes:
            convex_points = convex_points_between(c, d)
            for e in convex_points:
                if e not in cubes:
                    new_cubes.add(e)

    new_cubes = list(new_cubes)

    while len(new_cubes) > 0:
        current_pocket = []
        c = new_cubes.pop()
        current_pocket.append(c)
        new_found = True
        # adding things to this pocket of air (until no others are found)
        while new_found:
            new_found = False
            for c in new_cubes:
                c_not_in_pocket = True
                if c_not_in_pocket:
                    for d in current_pocket:
                        if overlap(c, d):
                            current_pocket.append(c)
                            new_cubes.remove(c)
                            new_found = True
                            c_not_in_pocket = False
                            break
            print(current_pocket)
        # now check whether pocket is 'inside' or 'outside'

        still_not_outside = True
        for c in current_pocket:
            if still_not_outside:
                if (c[0], c[1], c[2] + 1) not in current_pocket:
                    if (c[0], c[1], c[2] + 1) not in cubes:
                        still_not_outside = False
                        # current_pocket is outside!
                        break
                if (c[0], c[1], c[2] - 1) not in current_pocket:
                    if (c[0], c[1], c[2] - 1) not in cubes:
                        still_not_outside = False
                        # current_pocket is outside!
                        break
                if (c[0], c[1] + 1, c[2]) not in current_pocket:
                    if (c[0], c[1] + 1, c[2]) not in cubes:
                        still_not_outside = False
                        # current_pocket is outside!
                        break
                if (c[0], c[1] - 1, c[2]) not in current_pocket:
                    if (c[0], c[1] - 1, c[2]) not in cubes:
                        still_not_outside = False
                        # current_pocket is outside!
                        break
                if (c[0] + 1, c[1], c[2]) not in current_pocket:
                    if (c[0] + 1, c[1], c[2]) not in cubes:
                        still_not_outside = False
                        # current_pocket is outside!
                        break
                if (c[0] - 1, c[1], c[2]) not in current_pocket:
                    if (c[0] - 1, c[1], c[2]) not in cubes:
                        still_not_outside = False
                        # current_pocket is outside!
                        break

        if still_not_outside:
            # pocket must be inside
            print('adding pocket', current_pocket)
            for c in current_pocket:
                cubes.append(c)

    total_overlap = 0
    for c in cubes:
        for d in cubes:
            if overlap(c, d):
                total_overlap += 1

    print('Actual surface:', 6 * len(cubes) - total_overlap)

    print('Day18')
