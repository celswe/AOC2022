import numpy as np
import math
import re


def f(c):
    return c


f = open("6.txt", "r")
# print(f.read()) #f.readline()  f.read(x)
input = f.readlines()
f.close()

s = list(input[0])

for i in range(14,len(s)):
    s1 = s[i-14:i]
    s1 = set(s1)
    if len(s1) == 14:
        print(i)
        break


print('Day6')
