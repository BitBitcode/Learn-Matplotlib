import matplotlib.pyplot
# import matplotlib.pyplot as plt
import numpy
# import numpy as np


# 像素数据
a = numpy.array([0.31, 0.36, 0.42, 
                0.36, 0.43, 0.52,
                0.42, 0.52, 0.65]).reshape(3, 3)

matplotlib.pyplot.imshow(a, interpolation="none", cmap="bone", origin="upper")
matplotlib.pyplot.colorbar(shrink=0.9)
    # shrink：颜色条占默认值（与图片等高）的百分比



matplotlib.pyplot.xticks(())
matplotlib.pyplot.yticks(())

matplotlib.pyplot.show()
