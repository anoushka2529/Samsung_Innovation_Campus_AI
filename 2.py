N=10
a=56
d=3
sum1=0
for n in range(1,N+1):
    sum1=sum1+(a+(n-1)*d)
print("S10 = ",sum1,"by summation")

sum2 = 0
for n in range(1, N + 1):
    sum2 = sum2 + ((n * (n + 1)) / 2)
print("S10 = ", sum2, "by formula")