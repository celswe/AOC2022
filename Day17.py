import numpy as np
import math
import re
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import importlib
from itertools import chain, combinations

if __name__ == '__main__':
    # Getting the input
    filename = "17.txt"
    inp = open(filename, "r")
    # print(f.read()) #f.readline()  f.read(x)
    inputstring = list(inp.readlines()[0])
    inp.close()
    jets = inputstring

    # part 1

    shape_0 = np.ones((1, 4), int)
    shape_1 = np.ones((3, 3), int)
    shape_1[(2, 2, 0, 0), (2, 0, 2, 0)] = 0
    shape_2 = np.ones((3, 3), int)
    shape_2[(1, 1, 2, 2), (1, 0, 1, 0)] = 0
    shape_3 = np.ones((4, 1), int)
    shape_4 = np.ones((2, 2), int)
    shape = [shape_0, shape_1, shape_2, shape_3, shape_4]

    playing_field = np.zeros((2022 * 4, 7), int)
    current_jet_index = 0
    max_y = -1
    max_x = 6
    for s in range(2022):
        start_of_shape = [max_y + 4, 2]
        current_shape = shape[s % 5]
        end_of_shape = [start_of_shape[0] + current_shape.shape[0] - 1, start_of_shape[1] + current_shape.shape[1] - 1]
        stopped = False
        while not stopped:
            c = jets[current_jet_index]
            current_jet_index = (current_jet_index + 1) % len(jets)
            # print('starting at', start_of_shape, end_of_shape)
            if c == '<':
                # try move to left
                if start_of_shape[1] - 1 >= 0:  # check that boundary is not hit
                    if 2 not in playing_field[start_of_shape[0]:end_of_shape[0] + 1,  # check nothing else is hit
                                start_of_shape[1] - 1:end_of_shape[1]] + current_shape:
                        # move to left
                        start_of_shape[1] += -1
                        end_of_shape[1] += -1
                        # print(start_of_shape, end_of_shape)
            else:  # c == >, try move to right
                if end_of_shape[1] + 1 <= max_x:  # check that boundary is not hit
                    if 2 not in playing_field[start_of_shape[0]:end_of_shape[0] + 1,  # check nothing else is hit
                                start_of_shape[1] + 1:end_of_shape[1] + 2] + current_shape:
                        # move to right
                        start_of_shape[1] += 1
                        end_of_shape[1] += 1
                        # print(start_of_shape, end_of_shape)

            # fall down one step (if possible)
            if start_of_shape[0] - 1 >= 0:  # check that boundary at bottom is not hit
                if 2 not in playing_field[start_of_shape[0] - 1:end_of_shape[0],
                            # check nothing else is hit
                            start_of_shape[1]:end_of_shape[1] + 1] + current_shape:
                    # move to left
                    start_of_shape[0] += -1
                    end_of_shape[0] += -1
                    # print(start_of_shape, end_of_shape)
                else:
                    stopped = True
            else:
                stopped = True

            if stopped:
                playing_field[start_of_shape[0]:end_of_shape[0] + 1,
                start_of_shape[1]:end_of_shape[1] + 1] += current_shape
                max_y = max(max_y, end_of_shape[0])
                # plt.imshow(np.flipud(playing_field[0: max_y+1, :]))
                # print(np.flipud(playing_field[0: max_y+1, :]))
                # print(s, 'go to next block')
print(max_y + 1)

# part 2

# part 1

shape_0 = np.ones((1, 4), int)
shape_1 = np.ones((3, 3), int)
shape_1[(2, 2, 0, 0), (2, 0, 2, 0)] = 0
shape_2 = np.ones((3, 3), int)
shape_2[(1, 1, 2, 2), (1, 0, 1, 0)] = 0
shape_3 = np.ones((4, 1), int)
shape_4 = np.ones((2, 2), int)
shape = [shape_0, shape_1, shape_2, shape_3, shape_4]

extra_height = 0
current_jet_index = 0
max_y = -1
max_x = 6

y_reset_size = 1000
remembering_size = 100
playing_field = np.zeros((3 * y_reset_size, 7), int)  # np.zeros((len(inputstring * 10) * 4, 7), int)
last_pattern = np.zeros((remembering_size, 7), int)
last_s = -1
last_height = -1
jet_indices = []

for s in range(1000000000000):
    # finding information about current shape
    start_of_shape = [max_y + 4, 2]
    current_shape = shape[s % 5]
    end_of_shape = [start_of_shape[0] + current_shape.shape[0] - 1, start_of_shape[1] + current_shape.shape[1] - 1]
    stopped = False

    # check if we are are in a 'known state'
    # if s % 5 == 0:
    #
    #     print(s, (current_jet_index + 1) % len(jets))

    if (current_jet_index + 1) % len(jets) == 8 and s % 5 == 0:
        if np.array_equal(last_pattern, playing_field[max(0, max_y - remembering_size) : max_y + 1, :]):
            print('YES', last_s, s)
            diff_the_same = s - last_s
            remaining_s = 1000000000000 - s
            current_height = extra_height + max_y
            diff_in_height = current_height - last_height
            number_of_repeats = int(remaining_s / diff_the_same)
            new_s = s + number_of_repeats * diff_the_same
            new_extra_height = extra_height + number_of_repeats*diff_in_height
            break
            print('OK and now?')

        else:
            last_s = s
            last_pattern = playing_field[max_y - remembering_size: max_y + 1, :].copy()
            last_height = extra_height + max_y

        # plt.imshow(np.flipud(playing_field[max(0, max_y - 20): max_y + 1, :]))
        # plt.pause(.5)
        print(s, 'hallo, hier moeten we gaan regelen dat we dingen gaan herinneren')

    while not stopped:
        c = jets[current_jet_index]
        current_jet_index = (current_jet_index + 1) % len(jets)
        # print('starting at', start_of_shape, end_of_shape)
        if c == '<':
            # try move to left
            if start_of_shape[1] - 1 >= 0:  # check that boundary is not hit
                if 2 not in playing_field[start_of_shape[0]:end_of_shape[0] + 1,  # check nothing else is hit
                            start_of_shape[1] - 1:end_of_shape[1]] + current_shape:
                    # move to left
                    start_of_shape[1] += -1
                    end_of_shape[1] += -1
                    # print(start_of_shape, end_of_shape)
        else:  # c == >, try move to right
            if end_of_shape[1] + 1 <= max_x:  # check that boundary is not hit
                if 2 not in playing_field[start_of_shape[0]:end_of_shape[0] + 1,  # check nothing else is hit
                            start_of_shape[1] + 1:end_of_shape[1] + 2] + current_shape:
                    # move to right
                    start_of_shape[1] += 1
                    end_of_shape[1] += 1
                    # print(start_of_shape, end_of_shape)

        # fall down one step (if possible)
        if start_of_shape[0] - 1 >= 0:  # check that boundary at bottom is not hit
            if 2 not in playing_field[start_of_shape[0] - 1:end_of_shape[0],
                        # check nothing else is hit
                        start_of_shape[1]:end_of_shape[1] + 1] + current_shape:
                # move to left
                start_of_shape[0] += -1
                end_of_shape[0] += -1
                # print(start_of_shape, end_of_shape)
            else:
                stopped = True
        else:
            stopped = True

        if stopped:
            # update of playing field
            playing_field[start_of_shape[0]:end_of_shape[0] + 1, start_of_shape[1]:end_of_shape[1] + 1] += current_shape
            max_y = max(max_y, end_of_shape[0])

            if max_y > y_reset_size * 2:  # len(jets * 10):
                extra_height += y_reset_size  # len(jets * 5)
                new_playing_field = np.zeros((3 * y_reset_size, 7), int)  # np.zeros((len(jets * 10) * 4, 7), int)
                new_playing_field[0: 2*y_reset_size, :] = playing_field[y_reset_size: 3 * y_reset_size, :]
                # [0: len(jets) * 5 + 1, :] = playing_field[len(jets) * 5: len(jets) * 10 + 1, :]
                playing_field = new_playing_field
                max_y = max_y - y_reset_size  # len(jets * 5)
                #print('new playing field initiated', s, extra_height + max_y + 1, s / 1000000000000)
            # plt.imshow(np.flipud(playing_field[max(0, max_y - 20): max_y + 1, :]))
            # plt.pause(0.5)
            # print(np.flipud(playing_field[0: max_y+1, :]))
            # print(s, 'go to next block')

print('ending this sequence')
print(new_extra_height + max_y + 1)
extra_height = new_extra_height
for s in range(new_s, 1000000000000):
    # finding information about current shape
    start_of_shape = [max_y + 4, 2]
    current_shape = shape[s % 5]
    end_of_shape = [start_of_shape[0] + current_shape.shape[0] - 1, start_of_shape[1] + current_shape.shape[1] - 1]
    stopped = False

    while not stopped:
        c = jets[current_jet_index]
        current_jet_index = (current_jet_index + 1) % len(jets)
        # print('starting at', start_of_shape, end_of_shape)
        if c == '<':
            # try move to left
            if start_of_shape[1] - 1 >= 0:  # check that boundary is not hit
                if 2 not in playing_field[start_of_shape[0]:end_of_shape[0] + 1,  # check nothing else is hit
                            start_of_shape[1] - 1:end_of_shape[1]] + current_shape:
                    # move to left
                    start_of_shape[1] += -1
                    end_of_shape[1] += -1
                    # print(start_of_shape, end_of_shape)
        else:  # c == >, try move to right
            if end_of_shape[1] + 1 <= max_x:  # check that boundary is not hit
                if 2 not in playing_field[start_of_shape[0]:end_of_shape[0] + 1,  # check nothing else is hit
                            start_of_shape[1] + 1:end_of_shape[1] + 2] + current_shape:
                    # move to right
                    start_of_shape[1] += 1
                    end_of_shape[1] += 1
                    # print(start_of_shape, end_of_shape)

        # fall down one step (if possible)
        if start_of_shape[0] - 1 >= 0:  # check that boundary at bottom is not hit
            if 2 not in playing_field[start_of_shape[0] - 1:end_of_shape[0],
                        # check nothing else is hit
                        start_of_shape[1]:end_of_shape[1] + 1] + current_shape:
                # move to left
                start_of_shape[0] += -1
                end_of_shape[0] += -1
                # print(start_of_shape, end_of_shape)
            else:
                stopped = True
        else:
            stopped = True

        if stopped:
            # update of playing field
            playing_field[start_of_shape[0]:end_of_shape[0] + 1, start_of_shape[1]:end_of_shape[1] + 1] += current_shape
            max_y = max(max_y, end_of_shape[0])

            if max_y > y_reset_size * 2:  # len(jets * 10):
                extra_height += y_reset_size  # len(jets * 5)
                new_playing_field = np.zeros((3 * y_reset_size, 7), int)  # np.zeros((len(jets * 10) * 4, 7), int)
                new_playing_field[0: 2*y_reset_size, :] = playing_field[y_reset_size: 3 * y_reset_size, :]
                # [0: len(jets) * 5 + 1, :] = playing_field[len(jets) * 5: len(jets) * 10 + 1, :]
                playing_field = new_playing_field
                max_y = max_y - y_reset_size  # len(jets * 5)
                #print('new playing field initiated', s, extra_height + max_y + 1, s / 1000000000000)
            # plt.imshow(np.flipud(playing_field[max(0, max_y - 20): max_y + 1, :]))
            # plt.pause(0.5)
            # print(np.flipud(playing_field[0: max_y+1, :]))
            # print(s, 'go to next block')


print('Day17')
