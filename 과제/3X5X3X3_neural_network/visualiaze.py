import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def seperate_divsion(_div, origin):
    
    theta = np.linspace(0, np.pi / 2, 100)
    
    if (_div == 1):
        _r = 1
        a1 = np.array([0, _r])
        b1 = np.array([0, 0])
        _cos = _r * np.cos(theta)
        _sin = _r *np.sin(theta)
        
    elif (_div == 2):
        _r = 0.5
        a1 = np.array([0, _r])
        b1 = np.array([0, 0])
        _cos = _r *np.cos(theta)
        _sin = -1 * _r *np.sin(theta)
        
    elif (_div == 3):
        _r = 0.8
        a1 = np.array([0, -1 * _r])
        b1 = np.array([0, 0])
        _cos = -1 * _r *np.cos(theta)
        _sin = _r *np.sin(theta)

    
    _div_x = np.append(_cos, a1)
    _div_y = np.append(_sin, b1)
    
    for i in range(len(_div_x)):
        _div_x[i] += origin
        _div_y[i] += origin
    
    return _div_x, _div_y

dataset = np.loadtxt("./dataset.txt")
x = dataset[:,0]
y = dataset[:,1]
z = dataset[:,2]

testcase_xyz = np.loadtxt("./testcase_xyz.txt")
x2 = testcase_xyz[:,0]
y2 = testcase_xyz[:,1]
z2 = testcase_xyz[:,2]
result_R = testcase_xyz[:,3]
result_Y = testcase_xyz[:,4]
result_Z = testcase_xyz[:,5]

testcase_output = np.loadtxt("./testcase_output.txt", dtype=str)
cc = testcase_output

t = [[],[],[]]

d1 = [[],[],[]]
d2 = [[],[],[]]
d3 = [[],[],[]]

for i in range(len(x)):
    if (i % 3 == 0):
        d1[0].append(x[i])
        d1[1].append(y[i])
        d1[2].append(z[i])
    elif (i % 3 == 1):
        d2[0].append(x[i])
        d2[1].append(y[i])
        d2[2].append(z[i])
    elif (i % 3 == 2):
        d3[0].append(x[i])
        d3[1].append(y[i])
        d3[2].append(z[i])

theta = np.linspace(0, np.pi / 2, 100)
radius = 1
a = radius*np.cos(theta)
b = radius*np.sin(theta)

a1 = np.array([0, 1])
b1 = np.array([0, 0])

r_1 = np.array([2, 2])
r_2 = np.array([1, 1])
r_3 = np.array([0, 1])

r_4 = np.array([1, 1])
r_5 = np.array([2, 2])
r_6 = np.array([0, 1])

y_1 = np.array([1.5, 1.5])
y_2 = np.array([1, 1])
y_3 = np.array([1.5, 2.5])

y_4 = np.array([1, 1])
y_5 = np.array([0.5, 0.5])
y_6 = np.array([1.5, 2.5])

b_1 = np.array([1, 1])
b_2 = np.array([1.8, 1.8])
b_3 = np.array([3, 4])

b_4 = np.array([0.2, 0.2])
b_5 = np.array([1, 1])
b_6 = np.array([3, 4])

# origin line
e1 = np.array([1,1])
e2 = np.array([1,1])
e3 = np.array([0,4])

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')

# division 1
div_x, div_y = seperate_divsion(1, 1)
ax.plot(div_x, div_y, 0, color='red')
ax.plot(div_x, div_y, 1, color='red')

# division 2
div_x, div_y = seperate_divsion(2, 1)
ax.plot(div_x, div_y, 1.5, color='yellow')
ax.plot(div_x, div_y, 2.5, color='yellow')

# division 3
div_x, div_y = seperate_divsion(3, 1)
ax.plot(div_x, div_y, 3.0, color='blue')
ax.plot(div_x, div_y, 4.0, color='blue')

# draw origin line
ax.plot(e1,e2,e3,'k--', marker='o')

ax.plot(r_1,r_2,r_3,'r-')
ax.plot(r_4,r_5,r_6,'r-')
ax.plot(y_1,y_2,y_3,'yellow')
ax.plot(y_4,y_5,y_6,'yellow')
ax.plot(b_1,b_2,b_3,'blue')
ax.plot(b_4,b_5,b_6,'blue')

# draw dataset
# ax.scatter(d1[0], d1[1], d1[2], c='red')
# ax.scatter(d2[0], d2[1], d2[2], c='yellow')
# ax.scatter(d3[0], d3[1], d3[2], c='blue')

# draw test case
idx = 0
for i in range(len(x2)):
    if (i % 3 == 0) :
        idx += 1
    ax.text(x2[i],y2[i], z2[i], idx)
    if (result_R[i] == 1.0):
        ax.scatter(x2[i], y2[i], z2[i], c='red')

    if (result_Y[i] == 1.0):
        ax.scatter(x2[i], y2[i], z2[i], c='yellow')
    if (result_Z[i] == 1.0):
        ax.scatter(x2[i], y2[i], z2[i], c='blue')
# ax.scatter(ty[0], ty[1], ty[2], c='yellow')
# ax.scatter(tz[0], tz[1], tz[2], c='blue')
# ax.text(x2,y2,z2,cc)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()