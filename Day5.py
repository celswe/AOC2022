import numpy as np
import math
import re


def f(c):
    return c


f = open("5.txt", "r")
# print(f.read()) #f.readline()  f.read(x)
input = f.readlines()
f.close()
total = 0

split = [i for i, x in enumerate(input) if x == '\n'][0]
n = int(len(input[split - 1]) / 4)
stacks = [[] for i in range(n)]
for i in range(split - 1):
    line = input[split - i - 2]
    for j in range(n):
        if line[4 * j + 1] != ' ':
            stacks[j].append(line[4 * j + 1])

for i in range(split + 1, len(input)):
    line = input[i]
    (M, f, t) = re.findall('move ([0-9]+) from ([0-9]+) to ([0-9]+)', line)[0]
    temp = []
    for m in range(int(M)):
        p = stacks[int(f) - 1].pop()
        temp.append(p)
    for m in range(int(M)):
        p = temp.pop()
        stacks[int(t) - 1].append(p)

for i in range(n):
    print(stacks[i][-1])

print('Day4')
