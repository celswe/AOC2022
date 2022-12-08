import numpy as np

def decide(a, x):
    a = optionA[a]
    x = optionX[x]
    y = -10
    s = 0
    if x == 1:  #lose
        y = a - 1
        s += 0
    elif x == 2: #draw
        y = a
        s += 3
    elif x == 3: #win
        y = a - 2
        s += 6
    if y <= 0:
        y += 3
    s += y
    return s


def score(a, x):
    a = optionA[a]
    x = optionX[x]
    s = x
    if (a - x) % 3 == 0:
        s += 3
    if (a - x) % 3 == 1:
        s += 0
    if (a - x) % 3 == 2:
        s += 6
    return s


if __name__ == '__main__':
    f = open("2.txt", "r")
    # print(f.read()) #f.readline()  f.read(x)
    input = f.readlines()
    f.close()
    optionA = {'A': 1,
               'B': 2,
               'C': 3}
    optionX = {'X': 1,
               'Y': 2,
               'Z': 3}

    total = 0
    for line in input:
        ts = decide(line[0], line[2])
        #ts = score(line[0], line[2])
        total += ts
        print(line[0] + ', ' + line[2] + ' score: ' + str(ts))

    print(total)
    print('Day2')
