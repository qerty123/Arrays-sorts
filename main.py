from methods import *
from time import time

file = open('array.txt', 'r')
array = []
for i in file:
    array.append(int(i))
print('Starting array: ' + str(array))

# Bubble sort
st = time()
print('Bubble sort: ' + str(sort_bubble(array)))
print('Time: ' + "%s seconds" % (time() - st).__round__(4))

# Countion sort
st = time()
print('Countion sort: ' + str(sort_countion(array)))
print('Time: ' + "%s seconds" % (time() - st).__round__(4))

# Simple include sort
st = time()
print('Simple include sort: ' + str(sort_include(array)))
print('Time: ' + "%s seconds" % (time() - st).__round__(4))

# Simple eject sort
st = time()
print('Simple eject sort: ' + str(sort_eject(array)))
print('Time: ' + "%s seconds" % (time() - st).__round__(4))

# Shell sort
st = time()
print('Shell sort: ' + str(sort_shell(array)))
print('Time: ' + "%s seconds" % (time() - st).__round__(4))
