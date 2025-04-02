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

plt.show()
