import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3 * np.pi, 3 * np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.figure(figsize=(19.2, 14.4))
plt.plot(X, C, color='red', linestyle='--', label='Kosini')
plt.plot(X, S, color='blue', linestyle='-.', label='Sini')

plt.title('Kosini ja Sini -funktiot')
plt.xlabel('X-akseli (radianeissa)')
plt.ylabel('Y-akseli')
plt.legend()

ticks = np.arange(-3 * np.pi, 3.5 * np.pi, np.pi / 2)
labels = [r'$-3\pi$', r'$-5\pi/2$', r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$', r'$-\pi/2$', '0',
          r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$', r'$5\pi/2$', r'$3\pi$']

ticks = ticks[:len(labels)]

plt.xticks(ticks, labels)
plt.yticks([-1, 0, 1])

plt.show()
