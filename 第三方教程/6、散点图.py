import matplotlib.pyplot
# import matplotlib.pyplot as plt
import numpy
# import numpy as np

n = 1024
X = numpy.random.normal(0, 1, n)
Y = numpy.random.normal(0, 1, n)
T = numpy.arctan2(Y, X)

matplotlib.pyplot.scatter(X, Y, s=75, c=T, alpha=0.6)

matplotlib.pyplot.xlim((-1.5, 1.5))
matplotlib.pyplot.ylim((-1.5, 1.5))

matplotlib.pyplot.show()
