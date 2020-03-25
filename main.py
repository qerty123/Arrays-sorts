from methods import *
from time import time
from string import ascii_letters
from random import randint, choice
from progressbar import progressbar

iterations = 10
total = 2000
interval = 100
object_type = 'digits'  # digits, objects or strings
logs = False

results_bubble = [0]
results_countion = [0]
results_sinclude = [0]
results_seject = [0]
results_shell = [0]
results_tree = [0]
results_quicksort = [0]
results_merge = [0]
results_bitwise = [0]


class Objects:
    def __init__(self, data):
        self.data = data
        self.text0 = 'texttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttext'
        self.text1 = 'texttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttext'
        self.text2 = 'texttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttext'
        self.text3 = 'texttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttext'
        self.text4 = 'texttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttext'
        self.text5 = 'texttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttext'

    def __eq__(self, other):
        return self.data == other

    def __ne__(self, other):
        return self.data != other

    def __lt__(self, other):
        return self.data < other

    def __gt__(self, other):
        return self.data > other

    def __le__(self, other):
        return self.data <= other

    def __ge__(self, other):
        return self.data >= other

    def __floordiv__(self, other):
        return self.data // other

    def __mod__(self, other):
        return self.data % other


def make_sorts(array):
    # Bubble sort
    st = time()
    for i in range(iterations - 1):
        sort_bubble(array)
    if logs:
        print('Bubble sort: ' + str(sort_bubble(array)))
        print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_bubble.append((time() - st) / iterations)


    # Countion sort
    st = time()
    """for i in range(iterations - 1):
        sort_countion(array)
    if logs:
        print('Countion sort: ' + str(sort_countion(array)))
        print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))"""
    results_countion.append((time() - st) / iterations)


    # Simple include sort
    st = time()
    for i in range(iterations - 1):
        sort_include(array)
    if logs:
        print('Simple include sort: ' + str(sort_include(array)))
        print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))
    results_sinclude.append((time() - st) / iterations)


    # Simple eject sort
    st = time()
    """for i in range(iterations - 1):
        sort_eject(array)
    if logs:
        print('Simple eject sort: ' + str(sort_eject(array)))
        print('Time: ' + "%s seconds" % ((time() - st) / iterations).__round__(4))"""
    results_seject.append((time() - st) / iterations)


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
bar = progressbar.ProgressBar(maxval=total).start()
if not logs:
    print('Sort in progress: ')
for p in range(interval, total, interval):
    if logs:
        print('========== New iteration (' + str(p) + ') ==========')
    bar.update(p)
    array = []
    if object_type == 'objects':
        for o in range(0, p):
            array.append(Objects(randint(0, 100)))
    elif object_type == 'string':
        for o in range(0, p):
            array.append(''.join(choice(ascii_letters) for _ in range(10)))
    else:
        for o in range(0, p):
            array.append(randint(0, 100))
    make_sorts(array)
bar.finish()
print('Total time: ' + str((time() - tt).__round__(4)))

file = open('results_' + str(total) + '_' + object_type + '.txt', 'w')
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
