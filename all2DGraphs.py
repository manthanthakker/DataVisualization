import matplotlib.pyplot as plt
import numpy as np

x=np.random.rand(10)
y=np.random.rand(10)
x.sort()
y.sort()


x=x+.2

plt.subplot(311,facecolor='lightblue')
plt.title('Simple 2D graph')
plt.xlabel('x label')
plt.ylabel('y label')
plt.xscale('linear')
plt.plot(x,y,label='First')
#'linear','log','logtime','smlog'


plt.subplot(312,facecolor='lightblue')
plt.title('Simple 2D Bar chart')
plt.xlabel('x label')
plt.ylabel('y label')
plt.xscale('log')
xBar=[2,2,3,5,6,6,6,6,7,8]
yBar=[4,20,4,6,8,6,3,2,5,7]
plt.bar(xBar,yBar,label='bars')

plt.subplot(313,facecolor='lightblue')
plt.title('Simple 2D Histogram')
bins=[0,1,2,3,4,5,6,7,8,9,10]
plt.hist(xBar,bins,label='bars')
plt.subplots_adjust(left=0.1,right=0.9,wspace=0.7,hspace=0.9,bottom=0.1, top=0.9)

plt.legend()
plt.show()


