import numpy as np
import matplotlib.pyplot as plt

total = 2000
interval = 100
colors = ['#FF00FF', '#800080', '#FF0000', '#800000', '#FFFF00', '#808000', '#00FF00', '#008000', '#00FFFF', '#008080',
          '#0000FF', '#000080']
ox = []
for i in range(0, total, interval):
    ox.append(i)

file1 = open('results_' + str(total) + '_digits.txt', 'r')
file2 = open('results_' + str(total) + '_objects.txt', 'r')
file3 = open('results_' + str(total) + '_strings.txt', 'r')

plt.subplot(3, 1, 1)
plt.ylabel('Digits')
plt.title('Comparison of sorts')
plt.grid()
o = 0
for i in file1:
    array = []
    for p in i.split(' '):
        try:
            array.append(float(p))
        except:
            pass
    plt.plot(ox, array, linestyle='-', color=colors[o])
    o += 1
plt.legend(('Bubble', 'Countion', 'Simple include', 'Simple eject', 'Shell sort', 'Tree sort', 'Quick sort',
            'Merge sort', 'Bitwise'))

plt.subplot(3, 1, 2)
plt.ylabel('Objects')
plt.grid()
o = 0
for i in file2:
    array = []
    for p in i.split(' '):
        try:
            array.append(float(p))
        except:
            pass
    plt.plot(ox, array, linestyle='-', color=colors[o])
    o += 1
plt.legend(('Bubble', 'Countion', 'Simple include', 'Simple eject', 'Shell sort', 'Tree sort', 'Quick sort',
            'Merge sort', 'Bitwise'))

plt.subplot(3, 1, 3)
plt.ylabel('Strings')
plt.grid()
o = 0
for i in file3:
    array = []
    for p in i.split(' '):
        try:
            array.append(float(p))
        except:
            pass
    plt.plot(ox, array, linestyle='-', color=colors[o])
    o += 1

plt.xlabel('Number of elements')
plt.legend(('Bubble', 'Countion', 'Simple include', 'Simple eject', 'Shell sort', 'Tree sort', 'Quick sort',
            'Merge sort', 'Bitwise'))


plt.show()
