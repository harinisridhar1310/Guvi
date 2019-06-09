#harini
n,k=input().split()
k=int(k)
l=[]
m=[]
d=list(map(int,input().split()))
for i in range(0,len(d)):
	if(d[i]%2!=0):
		l.append(d[i])
	else:
		m.append(d[i])
print(l[k-1])
