import matplotlib.pyplot as plt

file = open('results.txt', 'r')
array0, array1, array2, array3, array4, array5 = [], [], [], [], [], []
o = 0
for i in file:
    if o == 0:
        array0.append(float(i))
        o += 1
    elif o == 1:
        array1.append(float(i))
        o += 1
    elif o == 2:
        array2.append(float(i))
        o += 1
    elif o == 3:
        array3.append(float(i))
        o += 1
    elif o == 4:
        array4.append(float(i))
        o += 1
    elif o == 5:
        array5.append(float(i))
        o = 0


ax = plt.subplot()
ax.set_facecolor('#DCDCDC')
ax.plot(array0, linestyle='-', color='#0000FF')  # bubble
ax.plot(array1, linestyle='-', color='#0000BB')  # countion
ax.plot(array2, linestyle='-', color='#FFFF00')  # include
ax.plot(array3, linestyle='-', color='#00FF00')  # eject
ax.plot(array4, linestyle='-', color='#00FFFF')  # shell
ax.plot(array5, linestyle='-', color='#FF00FF')  # tree

plt.show()
