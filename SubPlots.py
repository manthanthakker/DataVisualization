import matplotlib.pyplot as plt
import numpy as np

x=np.random.rand(10)
y=np.random.rand(10)
x.sort()
y.sort()

#plt.plot(x,y,'--')
x=x+.2


x=x+.2
plt.subplot(221,facecolor='lightblue')
plt.xlabel('x label')
plt.ylabel('y label')
plt.plot(x,y,'-')
plt.subplot(222,facecolor='lightblue')
plt.xlabel('x label')
plt.ylabel('y label')
x=x+.2
plt.plot(x,y,'X')
plt.subplot(223,facecolor='lightblue')
plt.xlabel('x label')
plt.ylabel('y label')
x=x+.2
plt.plot(x,y,'-')
plt.subplot(224,facecolor='lightblue')
plt.xlabel('x label')
plt.ylabel('y label')
x=x+.2
plt.plot(x,y,'X')
plt.title('Sample 2-d Graph')
plt.ylabel('Y axis  label')
plt.xlabel('X axis label')
plt.show()

## https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot
