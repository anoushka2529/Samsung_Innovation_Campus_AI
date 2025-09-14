'''formula for Tn is ar^(n-1)'''

a = int(input("Enter the value of a: "))
r = int(input("Enter the value of r: "))
n = int(input("Enter the value of n: "))
for i in range(1,n+1):
    t_n = a * r**(i-1)
    print(t_n)