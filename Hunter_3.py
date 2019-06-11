#harini
a=int(input())
b=list(map(int,input().split()))
c=[]
d=''
for i in range(0,len(b)):
	if(i==b[i]):
		c.append(b[i])
if(len(c)>0):
	c.sort()
	for j in range(0,len(c)):
		d=d+str(c[j])+" "
	print(d)
else:
	print(int(-1))
