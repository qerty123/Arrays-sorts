import random


def genarray(elements):
    file = open('array.txt', 'w')
    for i in range(elements):
        file.write(str(random.randint(-1000, 1000)) + '\n')
    file.close()
