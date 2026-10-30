import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)

y1 = (2 * x) + 1
y2 = (2 * x**2) + 2

plt.figure(figsize=(10, 5))
plt.plot(x, y1 , 'g', linewidth=2, label='y = 2x + 1')
plt.plot(x, y2 , 'b', linewidth=2, label='y = 2x^2 + 2')
plt.legend(loc='upper left')
plt.show()
