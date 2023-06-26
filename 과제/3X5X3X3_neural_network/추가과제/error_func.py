
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

load_txt = np.loadtxt("./error.txt")
x = np.arange(1, 1051)
y = load_txt[:]


plt.figure()
plt.plot(x, y, color="blue", linewidth=0.5)

plt.show()


