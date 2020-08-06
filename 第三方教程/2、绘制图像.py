import matplotlib.pyplot
# import matplotlib.pyplot as plt
import numpy
# import numpy as np

x = numpy.linspace(-5, 5, 100)

y1 = 1 / x
y2 = 2 / x
y3 = x
y4 = 2 * x
y5 = x * x
y6 = x * x * x

#【图1】将5个幂函数显示在一张图中，并规定大小为：500x500px（单位：100px）
# 同一个 figure() 函数后的所有 plot() 代码都将绘制在一张图中
# 如果不规定编号，将按照代码顺序一次生成；如果编号重复，则不会显示重复的第二张图
matplotlib.pyplot.figure(num = 1, figsize = (5, 5))   # 第一张序号设置为0，后面的序号将从1开始
matplotlib.pyplot.plot(x, y1)
matplotlib.pyplot.plot(x, y2)
matplotlib.pyplot.plot(x, y3)
matplotlib.pyplot.plot(x, y4)
matplotlib.pyplot.plot(x, y5)
matplotlib.pyplot.plot(x, y6)

#【图2】
matplotlib.pyplot.figure()
matplotlib.pyplot.plot(x, y3, linewidth = 0.5, linestyle = "-.")    # 设置线宽与线形
matplotlib.pyplot.plot(x, y1, color = "blue")   # 设置曲线颜色
matplotlib.pyplot.plot(x, y2, color = "red")

#【图3】
matplotlib.pyplot.figure()
matplotlib.pyplot.plot(x, y3, linewidth = 0.5, linestyle = "-")
matplotlib.pyplot.plot(x, y5, color = "blue")
matplotlib.pyplot.plot(x, y6, color = "green")


#【显示绘图结果】
# 不论有多少此绘图，只需要在最后加入函数 show() 即可全部显示
matplotlib.pyplot.show()
