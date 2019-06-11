#harini
x=int(input())
y=list(map(int,input().split()))
l=max(y)
e,f=0,0
for i in range(0,len(y)):
  for j in range(i+1,len(y)):
    if abs(y[i]+y[j])<l:
      e,f=y[i],y[j]
      l=abs(e+f)
print(e,f)
