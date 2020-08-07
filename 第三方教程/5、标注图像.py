import matplotlib.pyplot
# import matplotlib.pyplot as plt
import numpy
# import numpy as np


x = numpy.linspace(-3, 3, 50)
y = 2 * x + 1


#【绘图】
matplotlib.pyplot.figure(figsize = (8, 6))
matplotlib.pyplot.plot(x, y)


#【设置坐标轴】
ax = matplotlib.pyplot.gca()

ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")

ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))


#【标注某点】
# 设置标注点
x0 = 1
y0 = 2*x0 + 1
# 绘制一个散点
matplotlib.pyplot.scatter(x0, y0, s = 50, color = "red")
# 添加点在坐标轴的垂线段
matplotlib.pyplot.plot([x0, x0], [y0, 0], color = "grey", linestyle = "--")
matplotlib.pyplot.plot([0, x0], [y0, y0], color = "grey", linestyle = "--")
# 添加标注信息
#【方法1】(r"$2x+1=%s$"%y0, xy = (x0, y0)是必选参数)
matplotlib.pyplot.annotate(
                            r"$2x+1=%s$"%y0,                    # 标注文字
                            xy = (x0, y0),                      # 标注文字位置的基准点
                            xycoords = "data",                  # 偏移量基准于数据
                            xytext = (+30, -30),                # 标注文字在x、y轴方向上的偏移量（此时的原点位于上面设置的基准点）
                            textcoords = "offset points",       # 
                            fontsize = 16,                      # 标注字体
                            arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3, rad = 0.2")
                            # 标注箭头（线性、弯曲）
                            )

#【方法2】
matplotlib.pyplot.text(
                        -3.5, 3,
                        r"$This\ is\ a\ annotate.\ \mu_0\ \sigma_i$",
                        fontsize = 16
                        )


matplotlib.pyplot.show()