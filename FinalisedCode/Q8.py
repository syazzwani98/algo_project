import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy

y1 = [96,75,51,65,24,83,42,45]
y2 = [29,22,21,22,23,33,28,21]
x = numpy.arange(len(y1))

bar_width = 0.40
plt.bar(x, y1, width=bar_width, color='pink', zorder=2)
plt.bar(x +bar_width, y2, width=bar_width, color='purple', zorder=2)

plt.xticks(x + bar_width, ['Brazil','China','India','London','Russia','Spain','Thailand','US'])
plt.ylabel('Total words')
plt.xlabel('Country')
plt.title(' Comparison positive and negative words between country')

pink_patch = mpatches.Patch(color='pink', label='positive')
purple_patch = mpatches.Patch(color='purple', label='negative')
plt.legend(handles=[pink_patch,purple_patch])

plt.grid(axis='y')

plt.show()