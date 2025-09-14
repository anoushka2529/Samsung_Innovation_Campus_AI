#training a linar model
import numpy as np
import matplotlib.pyplot as plt
rng=np.random.default_rng(0)
x=np.linspace(-1,1,50)
y=3*x+2+rng.normal(0,0.1,50)
w,b=0.0,0.0
lr=0.5  #can be varied
epochs=100  #can be varied
def arrow(step):
    return "increase" if step>0 else "decrease" if step<0 else "-no change-"

hist_loss,hist_w=[],[]
for epoch in range(1,epochs+1):
    y_hat=w*x+b
    loss_signal=y_hat-y
    dL_dw=np.mean(loss_signal*x)
    dL_db=np.mean(loss_signal)

    step_w=-lr*dL_dw
    step_b=-lr*dL_db

    if epoch in(10,25,50,100):
        print(f" dLoss/dw={dL_dw:+.6f}->step_w={step_w:+.6f}=> w {arrow(step_w)}")
        print(f" dLoss/dw={dL_dw:+.6f}->step_b={step_w:+.6f}=> b {arrow(step_b)}")
    w+=step_w
    b+=step_b
    loss = 0.5 * np.mean((y_hat - y) ** 2)
    hist_loss.append(loss)
    hist_w.append(w)
print("\nTrue line ~ 3x+2")
print(f" Learned Line ~ {w:.3f}x+{b:.3f}")
        
fig,ax=plt.subplots(figsize=(5,4))
ax.plot(hist_w,hist_loss,marker='o',ms=3)
ax.set_xlabel('weight w')
ax.set_ylabel('Loss (0.5 *MSE )')
plt.tight_layout()
plt.show() 