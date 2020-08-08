# https://blog.csdn.net/jasonzhoujx/article/details/81780774

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np


# 绘制三角螺旋线
fig = plt.figure()

ax = plt.axes(projection='3d')

# 三维线的数据
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# 三维散点的数据
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

def g(x, y):
    return np.sin(x*x + y*y)


x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)


Z = g(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# 调整观察角度和方位角。这里将俯仰角设为60度，把方位角调整为35度
ax.view_init(60, 35)

plt.show()
