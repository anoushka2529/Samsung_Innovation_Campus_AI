import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,1001)
fx=(10+x**2)
gx=(3+x)
f1=10+gx**2
f2=3+fx
plt.plot(x,f1)
plt.plot(x,f2)
#plt.plot(x,fx)
plt.show()