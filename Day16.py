import numpy as np
import math
import re
import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from itertools import chain, combinations


#
# def powerset(iterable):
#     "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
#     s = list(iterable)
#     return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


class Subproblem:
    name = ''
    computed = False
    value = 0
    time_left_1 = 0
    time_left_2 = 0
    current_valve_1 = ''
    current_valve_2 = ''
    current_pressure_release_1 = 0
    current_pressure_release_2 = 0
    open_valves = set()
    usable_valves = set()
    next_best_subproblem = ''

    def __init__(self, current_valve_1, time_left_1, current_valve_2, time_left_2, open_valves,
                 current_pressure_release_1,
                 current_pressure_release_2, usable_valves):
        self.name = make_string_of_instance(current_valve_1, time_left_1, current_valve_2, time_left_2, 0, 0,
                                            open_valves)
        self.value = 0
        self.time_left_1 = time_left_1
        self.time_left_2 = time_left_2
        self.current_valve_1 = current_valve_1
        self.current_valve_2 = current_valve_2
        self.open_valves = open_valves
        self.current_pressure_release_1 = current_pressure_release_1
        self.current_pressure_release_2 = current_pressure_release_2
        self.usable_valves = usable_valves
        self.computed = False

    def compute(self):
        if self.computed:
            return self.value
        if self.time_left_1 > 0:
            # do nothing
            # new_subproblem_string = make_string_of_instance(start_valve, 0,
            #                                                 self.current_valve_2, self.time_left_2,
            #                                                 0, self.current_pressure_release_2,
            #                                                 self.open_valves)
            # if new_subproblem_string not in subproblems.keys():
            new_subproblem = Subproblem(start_valve, 0, self.current_valve_2,
                                        self.time_left_2, self.open_valves,
                                        0, self.current_pressure_release_2,
                                        self.usable_valves)
            #     subproblems[new_subproblem_string] = new_subproblem
            # else:
            #     new_subproblem = subproblems[new_subproblem_string]
            best_total_release = new_subproblem.compute() + self.time_left_1 * self.current_pressure_release_1
            self.next_best_subproblem = new_subproblem

            for v in self.usable_valves.values():
                d = self.current_valve_1.distances[v.name] + 1
                if v.name not in self.open_valves and d <= self.time_left_1:
                    # check if subproblem is in already created subproblem
                    new_open_valves = self.open_valves.copy()
                    new_open_valves.add(v.name)
                    # new_subproblem_string = make_string_of_instance(v, self.time_left_1 - d, self.current_valve_2,
                    #                                                 self.time_left_2,
                    #                                                 self.current_pressure_release_1 + v.flow,
                    #                                                 self.current_pressure_release_2, new_open_valves)
                    # if new_subproblem_string not in subproblems.keys():
                    new_subproblem = Subproblem(v, self.time_left_1 - d, self.current_valve_2, self.time_left_2,
                                                new_open_valves, self.current_pressure_release_1 + v.flow,
                                                self.current_pressure_release_2, self.usable_valves)
                    # subproblems[new_subproblem_string] = new_subproblem
                    # else:
                    #     new_subproblem = subproblems[new_subproblem_string]
                    if best_total_release < new_subproblem.compute() + d * self.current_pressure_release_1:
                        self.next_best_subproblem = new_subproblem
                        best_total_release = new_subproblem.compute() + d * self.current_pressure_release_1
                    else:
                        del new_subproblem
            self.value = best_total_release
        elif self.time_left_2 > 0:
            # do nothing
            new_subproblem = Subproblem(self.current_valve_1, self.time_left_1,
                                        self.current_valve_2, 0,
                                        self.open_valves, self.current_pressure_release_1,
                                        self.current_pressure_release_2, self.usable_valves)
            best_total_release = new_subproblem.compute() + self.time_left_2 * self.current_pressure_release_2
            self.next_best_subproblem = new_subproblem
            for v in self.usable_valves.values():
                d = self.current_valve_2.distances[v.name] + 1
                if v.name not in self.open_valves and d <= self.time_left_2:
                    # check if subproblem is in already created subproblem
                    new_open_valves = self.open_valves.copy()
                    new_open_valves.add(v.name)
                    #     new_subproblem_string = make_string_of_instance(self.current_valve_1, self.time_left_1, v,
                    #                                                     self.time_left_2 - d, self.current_pressure_release_1,
                    #                                                     self.current_pressure_release_2 + v.flow, new_open_valves)
                    #     if new_subproblem_string not in subproblems.keys():
                    #         new_subproblem = Subproblem(self.current_valve_1, self.time_left_1, v, self.time_left_2 - d,
                    #                                     new_open_valves, self.current_pressure_release_1,
                    #                                     self.current_pressure_release_2 + v.flow, self.usable_valves)
                    #         subproblems[new_subproblem_string] = new_subproblem
                    #     else:
                    #         new_subproblem = subproblems[new_subproblem_string]
                    new_subproblem = Subproblem(self.current_valve_1, self.time_left_1, v, self.time_left_2 - d,
                                                new_open_valves, self.current_pressure_release_1,
                                                self.current_pressure_release_2 + v.flow, self.usable_valves)
                    if best_total_release < new_subproblem.compute() + d * self.current_pressure_release_2:
                        self.next_best_subproblem = new_subproblem
                        best_total_release = new_subproblem.compute() + d * self.current_pressure_release_2
                    else:
                        del new_subproblem

            self.value = best_total_release
        else:
            self.value = 0
        self.computed = True
        # print(self.current_valve_1.name, self.time_left_1, self.current_valve_2.name, self.time_left_2,
        #      self.current_pressure_release_1, self.current_pressure_release_2, self.value)
        return self.value


class Valve:
    name = ''
    flow = 0
    neighbors = []

    def __init__(self, name, flow, neighbors):
        self.name = name
        self.flow = flow
        self.neighbors = neighbors
        self.distances = {}

    def compute_distances(self):
        not_yet_visited = {}
        distance = {}
        for v in valves.values():
            not_yet_visited[v.name] = 900
        not_yet_visited[self.name] = 0
        while len(not_yet_visited) > 0:
            v = min(not_yet_visited, key=not_yet_visited.get)
            distance[v] = not_yet_visited.pop(v)
            for nb in valves[v].neighbors:
                if nb in not_yet_visited.keys():
                    not_yet_visited[nb] = min(not_yet_visited[nb], distance[v] + 1)
        for v in valves_with_flow:
            self.distances[v] = distance[v]


def make_string_of_instance(current_valve_1, time_left_1, current_valve_2, time_left_2, current_flow_1, current_flow_2,
                            open_valves_input):
    s = str(current_valve_1.name) + ',' + str(time_left_1) + ',' + str(current_valve_2.name) + ',' + str(
        time_left_2) + str(current_flow_1) + ',' + str(current_flow_2) + ':'
    for v in open_valves_input:
        s += v + ','
    s += ':'

    return s


if __name__ == '__main__':
    # Getting the input
    filename = "16.txt"
    inp = open(filename, "r")
    # print(f.read()) #f.readline()  f.read(x)
    inputstring = inp.readlines()
    inp.close()

    valves = {}
    valves_with_flow = {}
    subproblems = {}

    for line in inputstring:
        line = line.strip()
        [name_new_valve, flow_new_valve, neighbors_new_valve] = \
            re.findall('Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnel[s]* lead[s]* to valve[s]* (.*)', line)[0]
        neighbors_new_valve = re.findall('([A-Z]{2})', neighbors_new_valve)
        new_valve = Valve(name_new_valve, int(flow_new_valve), neighbors_new_valve)
        valves[name_new_valve] = new_valve
        if int(flow_new_valve) > 0:
            valves_with_flow[name_new_valve] = new_valve

    print('hallo')
    for current_valve in valves_with_flow.values():
        current_valve.compute_distances()
    start_valve = valves['AA']
    start_valve.compute_distances()
    print('starting procedure')

    start_subproblem = Subproblem(start_valve, 30, start_valve, 0, set(), 0, 0, valves_with_flow)
    print(start_subproblem.compute())
    subproblems = {}
    start_subproblem = Subproblem(start_valve, 26, start_valve, 26, set(), 0, 0, valves_with_flow)
    print(start_subproblem.compute())

    #
    # temp_max = 0
    # for poss_set_me in list(powerset(valves_with_flow.values())):
    #     poss_set_me_dict = {}
    #     for s in poss_set_me:
    #         subproblems = {}
    #         poss_set_me_dict[s.name] = s
    #         temp = Subproblem(start_valve, 26, set(), 0, poss_set_me_dict).compute()
    #
    #         poss_set_ollie = {}
    #         for s in valves_with_flow.values():
    #             if s not in poss_set_me:
    #                 poss_set_ollie[s.name] =s
    #         subproblems = {}
    #         temp2 = Subproblem(start_valve, 26, set(), 0, poss_set_ollie).compute()
    #         print(temp_max, temp, temp2)
    #         temp_max = max(temp_max, temp+temp2)

    # print('Day16')
