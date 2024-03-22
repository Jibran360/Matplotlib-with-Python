import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.title("horizontal")
plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.grid(axis = 'y', linestyle = "--")
#plt.show()


#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.title("vertical")
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.grid(axis = 'x', linestyle = "--")
plt.show()