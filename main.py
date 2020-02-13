from methods import *
from time import time

file = open('array.txt', 'r')
array = []
for i in file:
    array.append(int(i))
print('Starting array: ' + str(array))

# Bubble sort
st = time()
for i in range(99):
    sort_bubble(array)
print('Bubble sort: ' + str(sort_bubble(array)))
print('Time: ' + "%s seconds" % ((time() - st) / 100).__round__(4))

# Countion sort
st = time()
for i in range(99):
    sort_countion(array)
print('Countion sort: ' + str(sort_countion(array)))
print('Time: ' + "%s seconds" % ((time() - st) / 100).__round__(4))

# Simple include sort
st = time()
for i in range(99):
    sort_include(array)
print('Simple include sort: ' + str(sort_include(array)))
print('Time: ' + "%s seconds" % ((time() - st) / 100).__round__(4))

# Simple eject sort
st = time()
for i in range(99):
    sort_eject(array)
print('Simple eject sort: ' + str(sort_eject(array)))
print('Time: ' + "%s seconds" % ((time() - st) / 100).__round__(4))

# Shell sort
st = time()
for i in range(99):
    sort_shell(array)
print('Shell sort: ' + str(sort_shell(array)))
print('Time: ' + "%s seconds" % ((time() - st) / 100).__round__(4))
