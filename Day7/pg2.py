import sympy as sp
import sympy as sp 
x=sp.Symbol('x')
m=x
n=x+1
f=m/n
diff_y=sp.diff(f,x)
print("Function of y =",f)
print("Derivative y =",diff_y)
print("Value of derivative at 2",diff_y.subs(f,2))