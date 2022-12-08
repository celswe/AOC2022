import numpy as np

if __name__ == '__main__':
    f = open("1.txt", "r")
    #print(f.read()) #f.readline()  f.read(x)
    input = f.readlines()
    f.close()

    #j = 0
    total = 0
    elfs = [0]
    for line in input:
        if line == '\n':
            #j = 0
            elfs.append(0)
        else:
            elfs[-1] += int(line)

    print(max(elfs))
    elfs.sort()
    print(sum(elfs[-3:])) #print sum of largest three
    print('Day1')