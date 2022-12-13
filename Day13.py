import numpy as np
import math
import re
import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import time


def compare(p1, p2):
    if type(p1) == int:
        if type(p2) == int:
            if p1 == p2:
                return -1
            elif p1 < p2:
                return 1  # 1 implies correct order
            else:
                return 0  # 0 implies wrong order
        else:  # p2 is a list
            p1 = [p1]
            return compare(p1, p2)
    else:  # p1 is a list
        if type(p2) == int:
            p2 = [p2]
            return compare(p1, p2)
        else: # p2 is a list
            for l in range(min(len(p1), len(p2))):
                compare_value = compare(p1[l],p2[l])
                if compare_value in [0, 1]:
                    return compare_value
            if len(p1) == len(p2):
                return -1 # draw
            elif len(p1) < len(p2):
                return 1 # win
            else:
                return 0



if __name__ == '__main__':
    # Getting the input
    filename = "13.txt"
    inp = open(filename, "r")
    # print(f.read()) #f.readline()  f.read(x)
    inputstring = inp.readlines()
    inp.close()
    total = 0


    # part 1

    for i in range(int(len(inputstring) / 3) + 1):
        packet_1 = eval(inputstring[3 * i].strip())
        packet_2 = eval(inputstring[3 * i + 1].strip())
        total += compare(packet_1, packet_2) * (i+1)
        # print(total, compare(packet_1, packet_2), packet_1, packet_2)

    # part 2
    packets = []
    for i in range(int(len(inputstring) / 3) + 1):
        packets.append(eval(inputstring[3 * i].strip()))
        packets.append(eval(inputstring[3 * i + 1].strip()))

    decode_packet_1 = [[2]]
    decode_index_1 = 1
    for packet in packets:
        if compare(packet, decode_packet_1) == 1:
            decode_index_1 += 1
            print(decode_packet_1, packet)


    decode_packet_2 = [[6]]
    decode_index_2 = 2
    for packet in packets:
        if compare(packet, decode_packet_2) == 1:
            decode_index_2 += 1
            print(decode_packet_2, packet)
    print(decode_index_1, decode_index_2, decode_index_1*decode_index_2)

    print('Day13')
