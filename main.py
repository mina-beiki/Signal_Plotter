from scipy import signal
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

start = -10
end = 10
step = 0.01
x1 = np.linspace(start, end, int((end-start)/step))
y1 = np.sin(x1)
#x1= np.linspace(start, end, num=(end-start)/step)
#y1= [3, 4, 5, 6, 7, 8]

#y2= [1, 2, 3, 4, 5, 6]
#x2= [3, 4, 5, 6, 7, 8]

style.use('ggplot')
plt.plot(x1, y1, color='red', label='Plot1')
#plt.plot(x2, y2, color='blue', label='PLot1')
plt.title('Plots')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.show()

#f, plt_arr=plt.subplot(3, sharex='col') #3 ta nemodar ke mehvare x ro share mikonan, f marboot be 3 ta nemoodar hast
#f.suptitle('Plots')

