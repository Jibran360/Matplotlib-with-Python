from cProfile import label
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]      # giving lables to chart pieces
myexplode = [0.2, 0, 0, 0]                                 # pulling Apple part away from chart
mycolors = ["black", "hotpink", "b", "#4CAF50"]            # specifing new colors for each wedge

plt.pie(y, labels = mylabels, startangle = 90, explode = myexplode, shadow = True, colors = mycolors)             # Start the first wedge at 90 degrees
plt.legend(title = "Four Fruits")
plt.show()