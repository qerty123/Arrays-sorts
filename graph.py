import matplotlib.pyplot as plt

colors = ['#FF00FF', '#800080', '#FF0000', '#800000', '#FFFF00', '#808000', '#00FF00', '#008000', '#00FFFF', '#008080', '#0000FF', '#000080']
#ax = plt.subplot()
file = open('results.txt', 'r')
o = 0
for i in file:
    array = []
    for p in i.split(' '):
        try:
            array.append(float(p))
        except:
            pass
    plt.plot(array, linestyle='-', color=colors[o])
    o += 1
#ax.set_facecolor('#DCDCDC')
plt.title('Comparison of sorts')
plt.xlabel('Elements')
plt.ylabel('Time')
plt.legend(('Bubble', 'Countion', 'Simple include', 'Simple eject', 'Shell sort', 'Tree sort', 'Quick sort', 'Merge sort', 'Bitwise'))
plt.grid()
plt.show()
