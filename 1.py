import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(10,6))
plt.axis("off")

plt.text(0.01,1.05,"2.1. Algebra",fontsize=14,color="white",
         bbox=dict(facecolor="navy",edgecolor="none",boxstyle="square,pad=0.5"))

plt.text(0.9,1.05,"UNIT 2",fontsize=12,color="white",
         bbox=dict(facecolor="navy",edgecolor="none",boxstyle="square,pad=0.5"),ha="right")

plt.text(0.01,0.95,"Algebra",fontsize=18,weight="bold",color="black")
body=("this is about algebra. ")
plt.text(0.01,0.75,body,fontsize=12,va="top")
x=np.linspace(-3,3,100)
y=x**2
ax_inset=fig.add_axes([0.05,0.05,0.2,0.2])
ax_inset.plot(x,y,color="blue")
ax_inset.axhline(0,color="black",lw=0.5)
ax_inset.axvline(0,color="black",lw=0.5)
ax_inset.set_title("y=x^2",fontsize=10)
ax_inset.set_xticks([])
ax_inset.set_yticks([])
plt.text(0.65,0.25,r"$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$",fontsize=16,color="black")
plt.show()