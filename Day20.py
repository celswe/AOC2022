import numpy as np
import math
import re
import matplotlib
import random

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import importlib
from itertools import chain, combinations


if __name__ == '__main__':
    # Getting the input
    filename = "20.txt"
    inp = open(filename, "r")
    # print(f.read()) #f.readline()  f.read(x)
    inputstring = inp.readlines()
    inp.close()

    current_list = []
    for line in inputstring:
        i = int(line.strip())
        if i == 0:
            current_list.append(i)
        elif i > 0:
            current_list.append(i + (random.random()/(10)))
        else:
            current_list.append(i - (random.random()/(10)))


    original_list = current_list.copy()
    length = len(original_list)
    print(current_list)
    # part 1
    for i in original_list:
        change_i = int(i)
        index_i = current_list.index(i)
        new_index = (index_i + change_i) % (length - 1)
        if new_index == 0 and change_i < 0:
            new_index = length-1
        if index_i < new_index:
            current_list[index_i: new_index] = current_list[index_i + 1: new_index + 1]
        elif new_index < index_i:
            current_list[new_index + 1: index_i + 1] = current_list[new_index: index_i]
        current_list[new_index] = i

    print('here is the answer:')
    index_of_0 = current_list.index(0)
    print(current_list[(index_of_0 + 1000) % length] + current_list[(index_of_0 + 2000) % length] + current_list[
        (index_of_0 + 3000) % length])


    # part 2 try 2
    current_list = []
    for line in inputstring:
        i = int(line.strip())
        if i == 0:
            current_list.append(i)
        elif i > 0:
            current_list.append(i + (random.random() / (100)))
        else:
            current_list.append(i - (random.random() / (100)))

    c = 811589153
    original_list = current_list.copy()
    length = len(original_list)

    for j in range(10):
        for i in original_list:
            change_i = int(i) * c
            index_i = current_list.index(i)
            new_index = (index_i + change_i) % (length - 1)
            if new_index == 0 and change_i < 0:
                new_index = length-1
            if index_i < new_index:
                current_list[index_i: new_index] = current_list[index_i + 1: new_index + 1]
            elif new_index < index_i:
                current_list[new_index + 1: index_i + 1] = current_list[new_index: index_i]
            current_list[new_index] = i

    print('here is the answer:')
    index_of_0 = current_list.index(0)
    print((int(current_list[(index_of_0 + 1000) % length]) + int(current_list[(index_of_0 + 2000) % length]) + int(current_list[
        (index_of_0 + 3000) % length])) * c)



    # part 2 try 1
    # current_list = []
    # j = 0.00002
    # for line in inputstring:
    #     i = int(line.strip())
    #     if i == 0:
    #         current_list.append(i)
    #     elif i > 0:
    #         current_list.append(round((i * 811589153) + j, 6)) #(random.random() / 10))
    #     else:
    #         current_list.append(round((i * 811589153) - j, 6)) #(random.random() / 10))
    #     j += 0.00002
    #
    # original_list = current_list.copy()
    # for j in range(10):
    #     for i in original_list:
    #         change_i = int(i)
    #         index_i = current_list.index(i)
    #         new_index = (index_i + change_i) % (length - 1)
    #         if new_index == 0 and change_i < 0:
    #             new_index = length-1
    #         if index_i < new_index:
    #             current_list[index_i: new_index] = current_list[index_i + 1: new_index + 1]
    #         elif new_index < index_i:
    #             current_list[new_index + 1: index_i + 1] = current_list[new_index: index_i]
    #         current_list[new_index] = i
    #
    # print('here is the answer:')
    # index_of_0 = current_list.index(0)
    # print(current_list[(index_of_0 + 1000) % length] + current_list[(index_of_0 + 2000) % length] + current_list[
    #     (index_of_0 + 3000) % length])
    print('Day20')
