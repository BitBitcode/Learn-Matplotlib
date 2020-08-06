import matplotlib.pyplot
# import matplotlib.pyplot as plt
import numpy
# import numpy as np

#【生成散点】
x = numpy.linspace(-5, 5, 100)
# 设置函数表达式
y = x * x

#【绘制曲线】
matplotlib.pyplot.plot(x, y)

#【显示绘图窗口】
matplotlib.pyplot.show()
