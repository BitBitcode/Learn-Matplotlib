import matplotlib.pyplot
# import matplotlib.pyplot as plt
import numpy
# import numpy as np

# 【生成数据】
x = numpy.linspace(-5, 5, 100)
# 设置函数表达式
y = x * x

# 【绘制曲线】
# 所有调用的绘图函数都将绘制在同一张图形中
matplotlib.pyplot.plot([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])    # 用列表的形式传入数据
matplotlib.pyplot.plot(x, y)                                # 用变量的形式传入数据

# 【显示绘图窗口】
matplotlib.pyplot.show()
