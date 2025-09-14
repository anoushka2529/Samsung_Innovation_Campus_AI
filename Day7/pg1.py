'''DEEP LEARNING
-contains an INPUT layer, an OUTPUT layer, and multiple HIDDEN layers in between.
-step 1:vectorization(sum of weight and input layers)y=w1x1+w2x2+...+wnxn where x are parameters and w are weights
-step 2:activation function(relu,sigmoid,tanh) which gives a z value
-step 3:uses another activation function and gives the final output y cap(predicted output)
*loss is calculated as y-y cap(must always be low) and to correct it backpropagation is used where the weights are adjusted using
the equation w new=w old-learning rate*derivative of loss function 
*global minumum is where the loss is the least(convergence) and the weight is optimal and the model is best trained 
*when eta or learning rate(usually 0.001) which is a hyper parameter is changed then the model converges faster and model performs 
better (basically rate of convergence is decided by eta)
*epoch is one complete forward and backward pass of all the training examples
*the goal is minimum number of epochs and high eta 
---------------------------------------------------------------------------------------------------
if the derivative is large then network is very sensitive then weight changees quickly 
if the derivative is small then network changes slowly that can lead to vanishing gradient problem
----------------------------------------------------------------------------------------------------
'''

#find the differentiation of f(x)=x^2+x+1    
import sympy as sp 
x=sp.Symbol('x')
m=x**2
n=x+1
f=m/n
diff_y=sp.diff(f,x)
print("Function of y =",f)
print("Derivative y =",diff_y)