import numpy as np
import math

def f(c):
    return c


if __name__ == '__main__':
    f = open("4.txt", "r")
    # print(f.read()) #f.readline()  f.read(x)
    input = f.readlines()
    f.close()
    total = 0

    for line in input:
        line = line.strip()
        s = [p.split('-') for p in line.split(',')]
#        if int(s[0][0]) == int(s[1][0]) and int(s[0][1]) == int(s[1][1]):
#            print('gelijk')
        if int(s[0][0]) <= int(s[1][0]) <= int(s[0][1]):
            total += 1
        elif int(s[0][0]) <= int(s[1][1]) <= int(s[0][1]):
            total += 1
        elif int(s[1][0]) <= int(s[0][0]) <= int(s[1][1]):
            total += 1
        elif int(s[1][0]) <= int(s[0][1]) <= int(s[1][1]):
            total += 1

    print(total)

    print('Day4')
