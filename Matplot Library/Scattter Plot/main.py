import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(1, 10, 50)
y = np.random.randint(10, 100, 50)
color  = np.random.randint(10, 100, 50)
plt.scatter(x, y,marker = "o",cmap = "viridis",c = color)
plt.colorbar()
plt.show()

