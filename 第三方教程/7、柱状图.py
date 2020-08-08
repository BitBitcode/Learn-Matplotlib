import matplotlib.pyplot
# import matplotlib.pyplot as plt
import numpy
# import numpy as np

n = 12

X = numpy.arange(n)
Y1 = (1-X/float(n)) * numpy.random.uniform(0.5, 1.0, n)
Y2 = (1-X/float(n)) * numpy.random.uniform(0.5, 1.0, n)


matplotlib.pyplot.xlim(-0.5, n)
matplotlib.pyplot.ylim(-1.25, 1.25)

matplotlib.pyplot.xticks(())
matplotlib.pyplot.yticks(())

matplotlib.pyplot.bar(X, +Y1, facecolor="#D6D6D6", edgecolor="#1342FF")
matplotlib.pyplot.bar(X, -Y2, facecolor="#F2F2F2", edgecolor="#FF1342")


#【添加数据标签】
for x, y in zip(X, Y1):     # zip() 将X, Y1打包为元组，传入到 x, y 中（否则将之传入一个数据）
    matplotlib.pyplot.text(x, y+0.05, "%0.2f" %y, ha="center", va="bottom")
# x, y 可以分别设置一个偏移量
# ha = horizontal alignment（水平对齐方式）:
# va = vertical alignment（垂直对齐方式）:
for x, y in zip(X, Y2):     # zip() 将X, Y1打包为元组，传入到 x, y 中（否则将之传入一个数据）
    matplotlib.pyplot.text(x, -y-0.05, "%0.2f" %y, ha="center", va="top")


matplotlib.pyplot.show()
