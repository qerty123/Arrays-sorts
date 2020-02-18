import random


def genarray(elements, name):
    file = open(name, 'w')
    for i in range(elements):
        file.write(str(random.randint(-10000, 10000)) + '\n')
    file.close()


genarray(100, 'array100.txt')
genarray(1000, 'array1000.txt')
genarray(5000, 'array5000.txt')
genarray(10000, 'array10000.txt')
genarray(20000, 'array20000.txt')
