from methods import *
from time import time

iterations = 30
results = []


def make_sorts(array):
    # Bubble sort
    st = time()
    for i in range(iterations - 1):
        sort_bubble(array)
    print('Bubble sort: ' + str(sort_bubble(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results.append((time() - st) / iterations)

    # Countion sort
    st = time()
    for i in range(iterations - 1):
        sort_countion(array)
    print('Countion sort: ' + str(sort_countion(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results.append((time() - st) / iterations)

    # Simple include sort
    st = time()
    for i in range(iterations - 1):
        sort_include(array)
    print('Simple include sort: ' + str(sort_include(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results.append((time() - st) / iterations)

    # Simple eject sort
    st = time()
    for i in range(iterations - 1):
        sort_eject(array)
    print('Simple eject sort: ' + str(sort_eject(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results.append((time() - st) / iterations)

    # Shell sort
    st = time()
    for i in range(iterations - 1):
        sort_shell(array)
    print('Shell sort: ' + str(sort_shell(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results.append((time() - st) / iterations)

    # Tree sort
    st = time()
    for i in range(iterations - 1):
        sort_tree(array)
    print('Tree sort: ' + str(sort_tree(array)))
    print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results.append((time() - st) / iterations)


file = open('array100.txt', 'r')
array = []
for o in file:
    array.append(int(o))
make_sorts(array)
file.close()

file = open('array1000.txt', 'r')
array = []
for o in file:
    array.append(int(o))
make_sorts(array)
file.close()

file = open('array5000.txt', 'r')
array = []
for o in file:
    array.append(int(o))
make_sorts(array)
file.close()

file = open('array10000.txt', 'r')
array = []
for o in file:
    array.append(int(o))
make_sorts(array)
file.close()

file = open('array20000.txt', 'r')
array = []
for o in file:
    array.append(int(o))
make_sorts(array)
file.close()

file = open('results.txt', 'w')
for o in results:
    file.write(str(o) + '\n')
file.close()

