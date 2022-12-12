import numpy as np
import math
import re
import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import time


# class Item:
#     divisors = []
#     rest = []
#
#     def __init__(self, worry_level, :


class Monkey:
    monkey_items = []
    operation = ''
    test = 0
    test_true_monkey = -1
    test_false_monkey = -1
    monkey_business = 0

    def __init__(self, items, operation, test, test_true, test_false):
        self.monkey_items = items
        self.operation = operation
        self.test = test
        self.test_true_monkey = test_true
        self.test_false_monkey = test_false
        self.monkey_business = 0

    def look_at_item(self):
        # get item from list of items
        current_item = self.monkey_items.pop(0)

        # apply operation
        old = current_item
        new = eval(self.operation)
        new = new % big_divisor
        # part 2: worry does not go down
        # new = int(new / 3)

        # do test
        if new % self.test == 0:
            monkey_to_go_to = self.test_true_monkey
        else:
            monkey_to_go_to = self.test_false_monkey

        return new, monkey_to_go_to


if __name__ == '__main__':
    # Getting the input
    filename = "11.txt"
    inp = open(filename, "r")
    # print(f.read()) #f.readline()  f.read(x)
    inputstring = inp.readlines()
    inp.close()

    number_of_monkeys = {"11t.txt": 4, "11.txt": 8}
    monkeys = []
    big_divisor = 1

    for i in range(number_of_monkeys[filename]):
        list_of_items = re.findall('([0-9]+)', inputstring[7 * i + 1].strip())
        text_operation = re.findall('Operation: new = (.*)', inputstring[7 * i + 2].strip())
        test_integer = re.findall('([0-9]+)', inputstring[7 * i + 3].strip())
        true_test_monkey = re.findall('([0-9]+)', inputstring[7 * i + 4].strip())
        false_test_monkey = re.findall('([0-9]+)', inputstring[7 * i + 5].strip())
        new_monkey = Monkey([int(x) for x in list_of_items], text_operation[0], int(test_integer[0]),
                            int(true_test_monkey[0]),
                            int(false_test_monkey[0]))
        monkeys.append(new_monkey)
        big_divisor = big_divisor * int(test_integer[0])

    for t in range(10000):
        for m in monkeys:
            for i in range(len(m.monkey_items)):
                [item, new_monkey] = m.look_at_item()
                monkeys[new_monkey].monkey_items.append(item)
                m.monkey_business += 1


        print(t, [m.monkey_business for m in monkeys])
    print('Day11')
