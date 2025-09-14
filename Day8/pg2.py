import sympy as sp
x=sp.Symbol('x')
f=x**2+3*x-1
diff_y=sp.diff(f,x)
print("derivative is",diff_y)
f_val=diff_y.subs(diff_y,5)
print(f_val)