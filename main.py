from methods import *
from time import time
from random import randint

iterations = 10
objects = False

results_bubble = []
results_countion = []
results_sinclude = []
results_seject = []
results_shell = []
results_tree = []
results_quicksort = []
results_merge = []
results_bitwise = []


class Objects:
    def __init__(self, data):
        self.data = data


def make_sorts(array):
    # Bubble sort
    st = time()
    for i in range(iterations - 1):
        sort_bubble(array)
    print('Bubble sort: ' + str(sort_bubble(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_bubble.append((time() - st) / iterations)

    # Countion sort
    st = time()
    for i in range(iterations - 1):
        sort_countion(array)
    print('Countion sort: ' + str(sort_countion(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_countion.append((time() - st) / iterations)

    # Simple include sort
    st = time()
    for i in range(iterations - 1):
        sort_include(array)
    print('Simple include sort: ' + str(sort_include(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_sinclude.append((time() - st) / iterations)

    # Simple eject sort
    st = time()
    for i in range(iterations - 1):
        sort_eject(array)
    print('Simple eject sort: ' + str(sort_eject(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_seject.append((time() - st) / iterations)

    # Shell sort
    st = time()
    for i in range(iterations - 1):
        sort_shell(array)
    print('Shell sort: ' + str(sort_shell(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_shell.append((time() - st) / iterations)

    # Tree sort
    st = time()
    for i in range(iterations - 1):
        sort_tree(array)
    print('Tree sort: ' + str(sort_tree(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_tree.append((time() - st) / iterations)

    # Quick sort
    st = time()
    for i in range(iterations - 1):
        sort_quick(array)
    print('Quick sort: ' + str(sort_quick(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_quicksort.append((time() - st) / iterations)

    # Merge sort
    for i in range(iterations - 1):
        sort_merge(array)
    print('Merge sort: ' + str(sort_merge(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_merge.append((time() - st) / iterations)

    # Bitwise sort
    for i in range(iterations - 1):
        sort_bitwise(array)
    print('Bitwise sort: ' + str(sort_bitwise(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_bitwise.append((time() - st) / iterations)


def make_str(array):
    string = ''
    for i in array:
        string += str(i.__round__(4)) + ' '
    string += '\n'
    return string


for p in range(100, 20000, 100):
    array = []
    if objects:
        for o in range(0, p):
            array.append(Objects(randint(-10000, 10000)))
    else:
        for o in range(0, p):
            array.append(randint(-10000, 10000))
    make_sorts(array)

file = open('results.txt', 'w')
file.write(make_str(results_bubble))
file.write(make_str(results_countion))
file.write(make_str(results_sinclude))
file.write(make_str(results_seject))
file.write(make_str(results_shell))
file.write(make_str(results_tree))
file.write(make_str(results_quicksort))
file.write(make_str(results_merge))
file.write(make_str(results_bitwise))
file.close()
