import matplotlib.pyplot
# import matplotlib.pyplot as plt
import numpy
# import numpy as np

from mpl_toolkits.mplot3d import Axes3D     # 绘制三维图需要导入专门的库


# 实例化对象
# 【规定】ins = instantiation：实例化，用ins来提示该变量是实例化操作所定义的
ins_fig = matplotlib.pyplot.figure()
ins_ax = Axes3D(ins_fig)


# 生成数据
X = numpy.arange(-4, 4, 0.25)
Y = numpy.arange(-4, 4, 0.25)
X, Y = numpy.meshgrid(X, Y)
F = numpy.sqrt(X**2 + Y**2)
# 高度值
Z = numpy.sin(F)


# 绘制三维图像
ins_ax.plot_surface(
    X, Y, Z,                                        # 传入数据
    rstride=1,                                      # 行间隔（row）
    cstride=1,                                      # 列间隔（column）
    cmap=matplotlib.pyplot.get_cmap("rainbow"),     # 图形色彩
    edgecolor="grey",                               # 网格色彩
    linewidths=0.5                                  # 网格线宽
)
# 绘制等高线图（从z、x、y三个不同的方向投影）
ins_ax.contourf(X, Y, Z, zdir="z", offset=-2, cmap="rainbow")
ins_ax.contourf(X, Y, Z, zdir="x", offset=+4, cmap="cool")
ins_ax.contourf(X, Y, Z, zdir="y", offset=-4, cmap="hot")


# 设置z轴区间
ins_ax.set_zlim(-2, 2)


# matplotlib.pyplot.xticks(())
# matplotlib.pyplot.yticks(())


# 设置坐标轴标签
ins_ax.set_xlabel('x')
ins_ax.set_ylabel('y')
ins_ax.set_zlabel('z')


# 设置坐标轴的位置
ins_ax.spines["bottom"].set_position(("data", 0))   # 注意：这里传入的参数是元组，不能省略里面的括号
ins_ax.spines["left"].set_position(("data", 0))


# 调整观察角度和方位角。(俯仰角, 方位角)
# 正方向的规定：右手坐标系的前提下，方向角满足x轴与y轴的右手螺旋方向
# 0°位置：俯仰角：xoy平面；方向角：与x轴重合
ins_ax.view_init(20, 120)

# 显示图像
matplotlib.pyplot.show()
