import matplotlib.pyplot as plt
import random
from itertools import count
from matplotlib.animation import FuncAnimation

x = []
y = []

idx = count()
def animate(i):
    x.append(next(idx))
    y.append(random.randint(0, 5))

    #clear axis method
    plt.cla()
    plt.plot(x, y)

#interval value in ms
ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.show()
