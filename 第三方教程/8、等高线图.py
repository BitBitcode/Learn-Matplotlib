import matplotlib.pyplot
# import matplotlib.pyplot as plt
import numpy
# import numpy as np


def f(x, y):
    return (1 - x/2 + x**5 + y**3) * numpy.exp(-x**2 - y**2)


def g(x, y):
    z = numpy.sin(x*x + y*y)
    return z


n = 1024
x = numpy.linspace(-5, 5, n)
y = numpy.linspace(-5, 5, n)

# 网格化
X, Y = numpy.meshgrid(x, y)

# for xi in x:
#     print("x = ", xi)
#     print("\n")

for Xi in X:
    print("X = ", Xi)
    print("\n")

# 绘制等高线彩图
matplotlib.pyplot.contourf(
    X, Y, f(X, Y),
    10,
    alpha=0.8,
    cmap=matplotlib.cm.cool
)
# contour()：等高线
# contourf()：带颜色的等高线
# cmap = colormap：颜色，hot，cool
# 数字参数：线条 = 数字 + 1，色块 = 数字 + 2


# 绘制等高线
C = matplotlib.pyplot.contour(
    X, Y, f(X, Y),
    10,
    colors="black",
    linewidths=0.5
)
# 数字参数最好与上面一致（相当于描线）


# 标注
matplotlib.pyplot.clabel(C, inline=True, fontsize=10)


# 不显示x、y轴及刻度
matplotlib.pyplot.xticks(())
matplotlib.pyplot.yticks(())


# 显示图像
matplotlib.pyplot.show()
