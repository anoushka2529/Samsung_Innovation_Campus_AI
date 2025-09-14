import numpy as np
import matplotlib.pyplot as plt

x1=np.linspace(0.1,4,401)
y1=np.log(x1)

x2=np.linspace(-0.9,4,501)
a=1/np.log(2)

y2=a*x2 
x3=np.linspace(-0.1,4,401)
y3=np.log(x1)

graph1,=plt.plot(x1,y1)
graph2,=plt.plot(x2,y2)
graph3,=plt.plot(x3,y3)

plt.legend(handles=(graph1,graph2),labels=(r'$y=log_2(x)$',r'$y=log_2(x+1)-1$'))
plt.show()