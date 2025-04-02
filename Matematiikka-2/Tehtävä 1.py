from matplotlib import pyplot as plt, patches
import numpy as np

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

angles_deg = [30, 45, 60, 90, 120, 150, 180, 270]
angles_rad = np.radians(angles_deg)

colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink', 'cyan']
texts = [r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$',
         r'$\frac{2\pi}{3}$', r'$\frac{5\pi}{6}$', r'$\pi$', r'$\frac{3\pi}{2}$']

x = np.cos(angles_rad)
y = np.sin(angles_rad)

plt.scatter(x, y, color=colors, marker='X')

for i in range(len(angles_rad)):
    plt.annotate(texts[i],
                 xy=(x[i], y[i]), xycoords='data',
                 xytext=(+10, +5), textcoords='offset points', fontsize=12,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.show()
