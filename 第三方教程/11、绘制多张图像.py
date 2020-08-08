import matplotlib.pyplot
# import matplotlib.pyplot as plt
import numpy
# import numpy as np


# 【方法1】
# 图1：四张图均匀分布
matplotlib.pyplot.figure(num=1)
# 子图1
matplotlib.pyplot.subplot(2, 2, 1)
matplotlib.pyplot.plot([0, 1], [0, 1])
# 子图2
matplotlib.pyplot.subplot(2, 2, 2)
matplotlib.pyplot.plot([0, 1], [1, 0])
# 子图3
matplotlib.pyplot.subplot(2, 2, 3)
matplotlib.pyplot.plot([-1, 0], [0, -1])
# 子图4
matplotlib.pyplot.subplot(2, 2, 4)
matplotlib.pyplot.plot([0, 1], [-1, 0])

# 图2：一张图占一行，另外三张图排在第二行
matplotlib.pyplot.figure(num=2)
# 子图1
matplotlib.pyplot.subplot(2, 1, 1)
matplotlib.pyplot.plot([0, 1], [0, 1])
# 子图2
matplotlib.pyplot.subplot(2, 3, 4)
matplotlib.pyplot.plot([0, 1], [1, 0])
# 子图3
matplotlib.pyplot.subplot(2, 3, 5)
matplotlib.pyplot.plot([-1, 0], [0, -1])
# 子图4
matplotlib.pyplot.subplot(2, 3, 6)
matplotlib.pyplot.plot([0, 1], [-1, 0])


# 【方法2】


# 【方法3】


# 【方法4】


# 显示图像
matplotlib.pyplot.show()
