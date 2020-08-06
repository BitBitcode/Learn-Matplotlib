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

# 对比二次函数与三次函数
matplotlib.pyplot.figure(figsize = (9, 6))
matplotlib.pyplot.plot(x, y3, linewidth = 0.8, linestyle = "-.")
matplotlib.pyplot.plot(x, y5)
matplotlib.pyplot.plot(x, y6)

#【设置 x、y 轴显示数据的区间】
matplotlib.pyplot.xlim(-1, 3)
matplotlib.pyplot.ylim(-1, 10)

#【设置 x、y 轴的标签】
matplotlib.pyplot.xlabel("time / s")
matplotlib.pyplot.ylabel("energy / J")

#【设置 x、y 轴刻度的区间、分度值大小以及将数字替换为文字】
# 注意：这里的区间只会影响刻度的区间，不会影响数据的区间，也就是说如果两个区间设置不一样，则刻度可能没有完全覆盖数据
new_ticks = numpy.linspace(0, 3, 12)
matplotlib.pyplot.xticks(new_ticks)
matplotlib.pyplot.yticks([0, 2, 4, 6, 8, 10], [r"$low\ power$", r"$warning$", "normal", r"$\alpha$", "high", "limit"])

#【设置坐标轴及刻度的位置】
# 获得当前的轴位置（类似于实例化一个类）
ax = matplotlib.pyplot.gca() # gca: get current axis
# 设置 x、y 轴刻度的位置（默认是左边和底边，但可能出错，所以手动设置一下）
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
# 去掉上边和右边的轴脊线（spine），即去掉默认边框的上边和右边
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
# 设置坐标轴的位置
ax.spines["bottom"].set_position(("data", 0))   # 注意：这里传入的参数是元组，不能省略里面的括号
ax.spines["left"].set_position(("data", 0))
    # 这里设置位置的方式还有：outward, axes（占另一个轴的百分比）


#【显示绘图结果】
# 不论有多少此绘图，只需要在最后加入函数 show() 即可全部显示
matplotlib.pyplot.show()
