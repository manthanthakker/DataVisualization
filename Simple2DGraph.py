import matplotlib.pyplot as plt
import numpy as np

x=np.random.rand(10)
y=np.random.rand(10)
x.sort()
y.sort()

plt.plot(x,y)
plt.title('Sample 2-d Graph')
plt.ylabel('Y axis  label')
plt.xlabel('X axis label')
plt.show()




## Refer https://matplotlib.org/gallery/pyplots/pyplot_simple.html#sphx-glr-gallery-pyplots-pyplot-simple-py
