import numpy as np
import math

def priority(c):
    p = ord(c)
    if p > 96:
        p = p - 96
    else:
        p = p - 64 + 26
    return p


if __name__ == '__main__':
    f = open("3.txt", "r")
    # print(f.read()) #f.readline()  f.read(x)
    input = f.readlines()
    f.close()
    total = 0

    for line in input:
        l = len(line)-1
        s1 = line[0:math.ceil(l/2)]
        s2 = line[math.ceil(l/2):l]
        for c in s1:
            if c in s2:
                total += priority(c)
                break

    print(total)

    total= 0
    k = len(input)
    for i in range(k)[0:k:3]:
        l1 = input[i]
        l2 = input[i+1]
        l3 = input[i+2]
        for c in l1:
            if c in l2:
                if c in l3:
                    total += priority(c)
                    break

    print('Day3')
