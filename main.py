from scipy import signal
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

# part 1:
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
# ----------------
# Signal 3:
# start = -5
# end = 10
# x1 = np.linspace(start, end, end - start + 1)
# y1 = np.exp(3*x1) * np.heaviside(x1+2, 1) + 2 * (np.heaviside(x1, 1) - np.heaviside(x1-1, 1))
# style.use('ggplot')
# plt.stem(x1, y1)
# plt.title('3')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.legend()
# plt.show()
# ----------------
# Signal 4:
# start = -5
# end = 5
# step = 0.01
# x1 = np.linspace(start, end, int((end - start)/step))
# y1 = np.heaviside(x1-2, 1) - np.heaviside(x1+2, 1)
# style.use('ggplot')
# plt.plot(x1, y1)
# plt.title('4')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.legend()
# plt.show()
# ----------------
# Signal 5:
# start = -10
# end = 10
# x1 = np.linspace(start, end, end-start+1)
# y1 = np.cos(3*x1)
# style.use('ggplot')
# plt.stem(x1, y1)
# plt.title('5')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.legend()
# plt.show()
# ----------------
# Signal 6:
# start = -10
# end = 10
# x1 = np.linspace(start, end, end-start+1)
# y1 = np.cos(3 * np.pi * x1)
# style.use('ggplot')
# plt.stem(x1, y1)
# plt.title('6')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.legend()
# plt.show()
#

# ----------------
# part 2:
# Signal 8:
# style.use('ggplot')
# start = -np.pi
# end = np.pi
# step = 0.01
# x1 = np.linspace(start, end, int((end - start) / step))
# y1 = np.sin((2 * x1)-3)
# plt.plot(x1, y1)
# plt.title('8')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.legend()
# plt.show()
# ----------------
# Signal 9:
start = -5
end = 10
x1 = np.linspace(start, end, end - start + 1)
x1new = ((-5 * x1) - 7)
y1 = -2 * (np.exp(3 * x1new) * np.heaviside(x1new + 2, 1) + 2 * (np.heaviside(x1, 1) - np.heaviside(x1 - 1, 1)))
style.use('ggplot')
plt.stem(x1, y1)
plt.title('9')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.show()
# ----------------
# Signal 10:
# style.use('ggplot')
# start = -np.pi
# end = np.pi
# step = 0.01
# x1 = np.linspace(start, end, int((end - start) / step))
# y1 = np.sin(-x1 + 3)
# plt.plot(x1, y1)
# plt.title('10')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.legend()
# plt.show()
# ----------------
