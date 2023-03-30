import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # len = 11
y = np.arange(4.5, 11, 1)  # len = 7
print(np.meshgrid(x, y))
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z)
plt.show()