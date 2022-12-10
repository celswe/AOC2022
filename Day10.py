import numpy as np
import math
import re
import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import time

signal_moments = (20, 60, 100, 140, 180, 220)


def update_signal(c, cur_x, sig):
    if c in signal_moments:
        sig += c * cur_x
    return sig


def find_position(c):
    column = (c-1) % 40
    row = int((c-1)/40)
    return [column, row]


def update_image(c, cur_x, cur_image):
    [col_c, row_c] = find_position(c)
    sprite_location = [pos_x for pos_x in [cur_x - 1, cur_x, cur_x + 1] if pos_x >= 0]
    print(c, cur_x)
    if col_c in sprite_location:
        print(c, col_c,row_c)
        cur_image[row_c][col_c] = 1
    return cur_image


if __name__ == '__main__':
    # Getting the input
    inp = open("10.txt", "r")
    # print(f.read()) #f.readline()  f.read(x)
    inputstring = inp.readlines()
    inp.close()

    signal = 0

    image = np.zeros((6, 40), int)
    x = 1
    cycle = 0
    # Reading in the data
    for line in inputstring:
        line = line.strip()
#        print(line)
        # find direction and number of steps
        if line == 'noop':
            cycle += 1
            update_signal(cycle, x, signal)
            update_image(cycle, x, image)
        else:
            [dx] = re.findall('addx (-*[0-9]+)', line)
            # first take a pause
            cycle += 1
            signal = update_signal(cycle, x, signal)
            update_image(cycle, x, image)
            # then change x and take a step
            cycle += 1
            signal = update_signal(cycle, x, signal)
            update_image(cycle, x, image)
            x += int(dx)
    print(signal)
    matplotlib.pyplot.imshow(image)
    print('Day10')
