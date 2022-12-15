import numpy as np
import math
import re
import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


def man_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


if __name__ == '__main__':
    # Getting the input
    filename = "15.txt"
    inp = open(filename, "r")
    # print(f.read()) #f.readline()  f.read(x)
    inputstring = inp.readlines()
    inp.close()

    xmin = 0
    ymin = 0
    xmax = 4000000
    ymax = 4000000

    total = 0
    intervals = [[] for x in range(ymax + 1)]
    for line in inputstring:
        line = line.strip()
        (current_sensor, closest_beacon) = re.findall('x=(-*[0-9]+), y=(-*[0-9]+)', line)
        current_sensor = [int(x) for x in current_sensor]
        closest_beacon = [int(x) for x in closest_beacon]
        distance = man_distance(current_sensor, closest_beacon)
        for current_y in range(max(ymin, current_sensor[1] - distance), min(ymax + 1, current_sensor[1] + distance + 1)):
            x_distance = distance - abs(current_sensor[1] - current_y)
            if x_distance >= 0:
                start_int = current_sensor[0] - x_distance
                end_int = current_sensor[0] + x_distance
                intervals[current_y].append([start_int, end_int])
        print('finished with another line')
    print('finished reading in intervals')
    #
    # places = set()
    # intervals.sort()
    # for (start_int, end_int) in intervals:
    #     for x in range(start_int, end_int +1):
    #         places.add(x)
    #
    # for line in inputstring:
    #     line = line.strip()
    #     (current_sensor, closest_beacon) = re.findall('x=(-*[0-9]+), y=(-*[0-9]+)', line)
    #     closest_beacon = [int(x) for x in closest_beacon]
    #     if closest_beacon[1] == checking_y:
    #         places.discard(closest_beacon[0])

    for y in range(ymax+1):
        intervals[y].sort()
        x = xmin
        for (start_int, end_int) in intervals[y]:
            if end_int >= x:
                if x < start_int - 1:
                    print(x + 1, y)
                    real_x = x +1
                    real_y = y
                    break
                else:
                    x = end_int
        print('not found in:', y)
    print('Day15')
