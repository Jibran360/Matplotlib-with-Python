import numpy as np
import matplotlib.pyplot as plt


# bar 1
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.bar(x, y, color = "red", width = 0.4)

# bar 2
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])


plt.subplot(1, 2, 2)
plt.barh(x, y, color = "yellow", height = 0.2)     # for barh() function use height instead of width.
plt.show()