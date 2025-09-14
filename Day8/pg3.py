import numpy as np
def sigmoid(z):return 1/(1+np.exp(-z))
rng=np.random.default_rng(0)
N=200
X0=rng.normal(loc=[-1,1],scale=0.6,size=(N//2,2))
X1=rng.normal(loc=[-1,1],scale=0.6,size=(N//2,2))
X=np.vstack([X0,X1])
y=np.hstack([np.zeros(N//2),np.ones(N//2)])
w=np.zeros(2)
b=0.0
lr=0.5
for epoch in range(1,101):
    p=sigmoid(X @ w + b)
    dL_dw=np.mean((p-y)[:,None]*X,axis=0)
    dL_db=np.mean(p-y)
    step_w=-lr*dL_dw
    step_b=-lr*dL_db
    w+=step_w; b+=step_b
    if epoch in(1,5,10,25,50,100):
        acc=np.mean((p>=0.5)==y)
        print(f"epoch {epoch:3d} | dL/dw={dL_dw} | step_w={step_w} | acc={acc:.2f}")