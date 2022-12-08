import numpy as np
import math
import re

if __name__ == '__main__':
    # Getting the input
    #    inp = open("7s.txt", "r")
    #    inputstring = inp.readlines()
    input2 = np.loadtxt("8.txt", dtype=str)
    M = np.array([list(x) for x in input2]).astype(int)

    (xmax, ymax) = M.shape
    H = np.zeros((xmax, ymax), bool)

    for i in range(xmax):
        current_max = -1
        for j in range(ymax):
            if M[i, j] > current_max:
                H[i, j] = True
                current_max = M[i, j]
        current_max = -1
        for j in range(ymax-1, -1, -1):
            if M[i, j] > current_max:
                H[i, j] = True
                current_max = M[i, j]

    for j in range(ymax):
        current_max = -1
        for i in range(xmax):
            if M[i, j] > current_max:
                H[i, j] = True
                current_max = M[i, j]
        current_max = -1
        for i in range(xmax-1, -1, -1):
            if M[i, j] > current_max:
                H[i, j] = True
                current_max = M[i, j]
    print(np.count_nonzero(H))

    # Part 2

    S = np.zeros((xmax, ymax), int)
    for i in range(xmax):
        last_occ = np.zeros(10, int)
        for j in range(ymax):
            last_seen = last_occ[M[i, j]]
            S[i, j] = j - last_seen
            for k in range(M[i, j]+1):
                last_occ[k] = j

        last_occ = np.zeros(10, int) + xmax-1
        for j in range(ymax-1, -1, -1):
            last_seen = last_occ[M[i, j]]
            trees_seen = last_seen - j
            S[i, j] = S[i, j] * trees_seen
            for k in range(M[i, j]+1):
                last_occ[k] = j

    for j in range(ymax):
        last_occ = np.zeros(10, int)
        for i in range(xmax):
            last_seen = last_occ[M[i, j]]
            trees_seen = i - last_seen
            S[i, j] = S[i,j] * trees_seen
            for k in range(M[i, j] + 1):
                last_occ[k] = i

        last_occ = np.zeros(10, int) + xmax - 1
        for i in range(xmax - 1, -1, -1):
            last_seen = last_occ[M[i, j]]
            trees_seen = last_seen - i
            S[i, j] = S[i, j] * trees_seen
            for k in range(M[i, j] + 1):
                last_occ[k] = i


    print(np.max(S))
    print('Day8')
