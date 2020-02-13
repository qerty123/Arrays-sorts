import random

file = open('array.txt', 'w')
for i in range(100):
    file.write(str(random.randint(-1000, 1000)) + '\n')
file.close()
