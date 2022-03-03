from scipy import signal
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

# Signal 1:
# style.use('ggplot')
# start = -np.pi
# end = np.pi
# step = 0.01
# x1 = np.linspace(start, end, int((end - start) / step))
# y1 = np.sin(x1)
# plt.plot(x1, y1)
# plt.title('1')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.legend()
# plt.show()
# ----------------
# Signal 2:
# start1 = -5
# end1 = -1
# start2 = 0
# end2 = 5
# x1 = np.linspace(start1, end1, end1-start1+1)
# y1 = -x1-1
# x2 = np.linspace(start2, end2, end2-start2+1)
# y2 = np.power(x2, 2)
# style.use('ggplot')
# plt.stem(x1, y1)
# plt.stem(x2, y2)
# plt.title('2')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.legend()
# plt.show()
