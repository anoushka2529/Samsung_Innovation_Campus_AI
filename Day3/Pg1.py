import matplotlib.pyplot as plt
import numpy as np


plt.subplot(3,1,2)
x=np.linspace(-2,2,100)
y_sin=np.sin(x)
plt.plot(x,y_sin,color='orange',label='sine')
plt.show()

y_cos=np.acos(x)
plt.plot(x,y_cos,color='green',label='cosine')
plt.show()
plt.legend()
plt.show()