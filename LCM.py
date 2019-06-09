#harini
a=list(map(int,input().split()))
x=a[0]
y=a[1]
if x > y:
    g=x
else:
    g=y
while(True):
    if((g%x==0) and (g%y==0)):
        lcm=g
        break
    g+=1
print(lcm)
