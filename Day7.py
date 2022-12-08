import numpy as np
import math
import re


class Folder:
    subfolders = []
    filesizes = 0
    computed = False
    size = 0
    parent = None
    name = ''
    totalsize = 0

    def __init__(self, name, parent):
        self.filesizes = 0
        self.subfolders = []
        self.computed = False
        self.size = 0
        self.name = name
        self.parent = parent
        self.totalsize = 0

    def addFolder(self, child):
        self.subfolders.append(child)
        child.parent = self

    def addfile(self, file_size):
        self.filesizes += file_size

    def computesize(self):
        if not self.computed:
            total = self.filesizes
            for child in self.subfolders:
                total += child.computesize()
            self.computed = True
            self.size = total
        return self.size

    def totalcomputesize(self):
        total = 0
        for child in self.subfolders:
            total += child.totalcomputesize()
        if self.size > 100000:
            self.totalsize = total
        else:
            self.totalsize = self.size + total
        return self.totalsize

    def totaldirectories(self):
        total = 1
        for child in self.subfolders:
            total += child.totaldirectories()
        return total

    def candelete(self, space):
        if self.size >= space:
            m = self.size
            for f in self.subfolders:
                m = min(m, f.candelete(space))
            return m
        else:
            return totalspace


if __name__ == '__main__':
    # Getting the input
    inp = open("7s.txt", "r")
    # print(f.read()) #f.readline()  f.read(x)
    inputstring = inp.readlines()
    inp.close()

    # Making root folder
    root = Folder('/', None)
    current = root

    # Reading in the data
    for line in inputstring:
        line = line.strip()

        # check if it is a cd
        (found) = re.findall('\$ cd (.+)', line)
        if len(found) == 1:
            # state = 'cd'
            if found[0] == '/':
                current = root
            elif found[0] == '..':
                current = current.parent
            else:
                for f in current.subfolders:
                    if f.name == found[0]:
                        current = f
                        break

        # check if it is a ls
        elif line == '$ ls':
            # state = 'ls'
            state = 'ls'

        # else, we are in a ls state
        else:
            (found) = re.findall('dir (.+)', line)
            if len(found) == 1:
                f = Folder(found[0], current)
                current.addFolder(f)
            else:
                [(s, f)] = re.findall('([0-9]+) (.+)', line)
                current.filesizes += int(s)

    # compute the sizes
    print(root.computesize())
    print(root.totalcomputesize())

    totalspace = 70000000
    usedspace = root.computesize()
    freespace = totalspace - usedspace
    neededspace = 30000000 - freespace

    print(root.candelete(neededspace))

    print('Day7')
