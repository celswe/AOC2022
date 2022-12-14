import numpy as np
import math
import re
import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Getting the input
    filename = "14.txt"
    inp = open(filename, "r")
    # print(f.read()) #f.readline()  f.read(x)
    inputstring = inp.readlines()
    inp.close()

    map = np.zeros((1000, 1000), bool)
    maxy = 0
    for line in inputstring:
        line = line.strip()
        (points) = re.findall('([0-9]+),([0-9]+)', line)
        for i in range(len(points) - 1):
            p1x = int(points[i][0])
            p1y = int(points[i][1])
            p2x = int(points[i + 1][0])
            p2y = int(points[i + 1][1])
            maxy = max(maxy, p2y, p1y)

            if p1x == p2x:
                for j in range(min(p1y, p2y), max(p1y, p2y) + 1):
                    map[p1x, j] = True
            else:
                for j in range(min(p1x, p2x), max(p1x, p2x) + 1):
                    map[j, p1y] = True
    bottom = maxy+2
    map[:, bottom] = True

    finished = False
    total = 0
    while not finished:
        # print('new sand, total =', total)
        current_x = 500
        current_y = 0
        falling = True
        while falling and not finished:
            if not map[current_x, current_y + 1]:
                current_y += 1
            elif not map[current_x - 1, current_y + 1]:
                current_x += -1
                current_y += 1
            elif not map[current_x + 1, current_y + 1]:
                current_x += 1
                current_y += 1
            else:
                if current_x == 500 and current_y == 0:
                    finished = True
                else:
                    total = total + 1
                    print(current_x, current_y, total)
                    map[current_x, current_y] = True
                    falling = False

    print(total)
    print('Day14')
