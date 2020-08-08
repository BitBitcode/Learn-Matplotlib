import matplotlib.pyplot
# import matplotlib.pyplot as plt
import numpy
# import numpy as np

n = 1024
X = numpy.random.normal(0, 5, n)  # 平均数为0，方差为1的正态分布
Y = numpy.random.normal(0, 5, n)
T = numpy.arctan2(Y, X)

matplotlib.pyplot.scatter(X, Y, s=75, c=T, alpha=0.6)
# matplotlib.pyplot.scatter(numpy.arange(5), numpy.arange(5))

matplotlib.pyplot.xlim((-5, 5))
matplotlib.pyplot.ylim((-5, 5))

# 去掉刻度
matplotlib.pyplot.xticks(())
matplotlib.pyplot.yticks(())

matplotlib.pyplot.show()
