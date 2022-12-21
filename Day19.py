import numpy as np
import math
import re
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import importlib
from itertools import chain, combinations


class Subproblem:
    robots = np.array([0, 0, 0, 0])
    resources = np.array([0, 0, 0, 0])
    time = 0
    best_geodes = -1
    best_subproblem = []
    computed = False

    def __init__(self, robots, resources, time):
        self.robots = robots
        self.resources = resources
        self.time = time
        self.best_geodes = -1
        self.best_subproblem = []
        self.computed = False

    def compute(self):
        if self.computed:
            # print('reused value')
            return self.best_geodes
        if self.time == time_limit:
            return 0

        # do nothing
        do_nothing_resources = self.resources + self.robots
        self.best_geodes, self.best_subproblem = self.compute_subproblem(self.robots, do_nothing_resources, self.time + 1)

        # make geodes robot
        if self.enough_resources(3):
            geode_resources = self.resources - costs[3] + self.robots
            geode_robots = self.robots + np.array([0, 0, 0, 1])
            geode_geodes, geode_subproblem = self.compute_subproblem(geode_robots, geode_resources, self.time + 1)

            if self.best_geodes < geode_geodes:
                self.best_geodes = geode_geodes
                self.best_subproblem = geode_subproblem

        # make obsidian robot
        if self.enough_resources(2):
            ob_resources = self.resources - costs[2] + self.robots
            ob_robots = self.robots + np.array([0, 0, 1, 0])
            ob_geodes, ob_subproblem = self.compute_subproblem(ob_robots, ob_resources, self.time + 1)
            if self.best_geodes < ob_geodes:
                self.best_geodes = ob_geodes
                self.best_subproblem = ob_subproblem

        # make clay robot
        if self.enough_resources(1):
            clay_resources = self.resources - costs[1] + self.robots
            clay_robots = self.robots + np.array([0, 1, 0, 0])
            clay_geodes, clay_subproblem = self.compute_subproblem(clay_robots, clay_resources, self.time + 1)
            if self.best_geodes < clay_geodes:
                self.best_geodes = clay_geodes
                self.best_subproblem = clay_subproblem

        # make ore robot
        if self.enough_resources(0):
            ore_resources = self.resources - costs[0] + self.robots
            ore_robots = self.robots + np.array([1, 0, 0, 0])
            ore_geodes, ore_subproblem = self.compute_subproblem(ore_robots, ore_resources, self.time + 1)
            if self.best_geodes < ore_geodes:
                self.best_geodes = ore_geodes
                self.best_subproblem = ore_subproblem

        self.best_geodes += self.robots[3]
        if self.time < 5:
            print('subproblem: ', '\t', self.time, '\t',self.robots, '\t',self.resources, '\t',self.best_geodes)
        self.computed = True
        return self.best_geodes

    def enough_resources(self, r):
        if self.resources[0] >= costs[r][0] and self.resources[1] >= costs[r][1] and self.resources[2] >= costs[r][2]:
            return True
        return False

    def compute_subproblem(self, new_robots, new_resources, new_time):
        for i in range(4):
            new_resources[i] = min(new_resources[i], max(costs[:, i]) * (time_limit - new_time))
        sub_name = subproblem_name(new_robots, new_resources, new_time)
        if sub_name not in subproblems.keys():
            new_subproblem = Subproblem(new_robots, new_resources, new_time)
            subproblems[sub_name] = new_subproblem
        else:
            new_subproblem = subproblems[sub_name]
        return new_subproblem.compute(), new_subproblem


def subproblem_name(robots, resources, time):
    s = 'time = ' + str(time)
    s += 'robots: '
    for i in range(4):
        s += str(robots[i]) + ','
    s += ' resources: '
    for i in range(4):
        s += str(resources[i]) + ','
    return s


if __name__ == '__main__':
    # Getting the input
    filename = "19.txt"
    inp = open(filename, "r")
    # print(f.read()) #f.readline()  f.read(x)
    inputstring = inp.readlines()
    inp.close()

    time_limit = 32 # 24
    costs = np.array([[0, 0, 0, 0] for i in range(4)])
    for blueprint in range(3): # range(len(inputstring)):
        line = inputstring[blueprint].strip()
        ore_line = re.findall('(Each ore robot .+?\.)', line)[0]
        clay_line = re.findall('(Each clay robot .+?\.)', line)[0]
        obsidian_line = re.findall('(Each obsidian robot .+?\.)', line)[0]
        geode_line = re.findall('(Each geode robot .+?\.)', line)[0]
        costs[0][0] = int(re.findall('([0-9]+) ore', ore_line)[0])
        costs[1][0] = int(re.findall('([0-9]+) ore', clay_line)[0])
        costs[2][0] = int(re.findall('([0-9]+) ore', obsidian_line)[0])
        costs[2][1] = int(re.findall('([0-9]+) clay', obsidian_line)[0])
        costs[3][0] = int(re.findall('([0-9]+) ore', geode_line)[0])
        costs[3][2] = int(re.findall('([0-9]+) obsidian', geode_line)[0])

        start = Subproblem(np.array([1, 0, 0, 0]), np.array([0, 0, 0, 0]), 0)

        subproblems = {}

        # for t in reversed(range(26)):
        #     for nr_ore in range(time_limit - t):
        #         for nr_clay in range(time_limit - t):
        #             for nr_ob in range(time_limit - t):
        #                 for nr_geode in range(time_limit - t):
        #
        print(blueprint, start.compute())

    print('Day19')
