#harini
a=list(map(int,input().split()))
n=a[0]
k=a[1]
l=[]
for i in range(1,1000):
	if(n%i==0 and k%i==0):
		l.append(i)
print(max(l))
