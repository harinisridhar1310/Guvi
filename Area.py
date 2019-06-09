#harini
import decimal
x=list(map(float,input().split()))
a=x[0]
b=x[1]
c=a*b
d=(decimal.Decimal(c))
print(round(d,5))
