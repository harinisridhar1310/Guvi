#harini
n,k=input().split()
n=int(n)
k=int(k)
c=0
b=list(map(int,input().split()))
for i in range(0,n-1):
	if(k==b[i]):
		c=c+1
if c>0:
	print("Yes")
else:
	print("No")
