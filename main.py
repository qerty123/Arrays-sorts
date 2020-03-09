from methods import *
from time import time
from random import randint
from progressbar import progressbar

iterations = 10
total = 5000
objects = False
logs = False

results_bubble = []
results_countion = [0]
results_sinclude = []
results_seject = [0]
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
    if logs:
        print('Bubble sort: ' + str(sort_bubble(array)))
        print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_bubble.append((time() - st) / iterations)

    """
    # Countion sort
    st = time()
    for i in range(iterations - 1):
        sort_countion(array)
    if logs:
        print('Countion sort: ' + str(sort_countion(array)))
        print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_countion.append((time() - st) / iterations)
    """

    # Simple include sort
    st = time()
    for i in range(iterations - 1):
        sort_include(array)
    if logs:
        print('Simple include sort: ' + str(sort_include(array)))
        print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_sinclude.append((time() - st) / iterations)

    """
    # Simple eject sort
    st = time()
    for i in range(iterations - 1):
        sort_eject(array)
    if logs:
        print('Simple eject sort: ' + str(sort_eject(array)))
        print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_seject.append((time() - st) / iterations)
    """

    # Shell sort
    st = time()
    for i in range(iterations - 1):
        sort_shell(array)
    if logs:
        print('Shell sort: ' + str(sort_shell(array)))
        print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_shell.append((time() - st) / iterations)

    # Tree sort
    st = time()
    for i in range(iterations - 1):
        sort_tree(array)
    if logs:
        print('Tree sort: ' + str(sort_tree(array)))
        print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_tree.append((time() - st) / iterations)

    # Quick sort
    st = time()
    for i in range(iterations - 1):
        sort_quick(array)
    if logs:
        print('Quick sort: ' + str(sort_quick(array)))
        print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_quicksort.append((time() - st) / iterations)

    # Merge sort
    for i in range(iterations - 1):
        sort_merge(array)
    if logs:
        print('Merge sort: ' + str(sort_merge(array)))
        print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_merge.append((time() - st) / iterations)

    # Bitwise sort
    for i in range(iterations - 1):
        sort_bitwise(array)
    if logs:
        print('Bitwise sort: ' + str(sort_bitwise(array)))
        print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_bitwise.append((time() - st) / iterations)


def make_str(array):
    string = ''
    for i in array:
        string += str(i.__round__(4)) + ' '
    string += '\n'
    return string


tt = time()
if not logs:
    bar = progressbar.ProgressBar(maxval=total).start()
    print('Sort in progress: ')
for p in range(100, total, 100):
    if logs:
        print('========== New iteration (' + str(p) + ') ==========')
    else:
        bar.update(p)
    array = []
    if objects:
        for o in range(0, p):
            array.append(Objects(randint(-10000, 10000)))
    else:
        for o in range(0, p):
            array.append(randint(-10000, 10000))
    make_sorts(array)
bar.finish()
print('Total time: ' + str((time() - tt).__round__(4)))

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
