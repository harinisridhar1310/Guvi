#harini
a=int(input())
b=list(map(int,input().split()))
c=''
for i in range(0,len(b)):
	if((i%2==0 and b[i]%2!=0)or(i%2!=0 and b[i]%2==0)):
		c=c+str(b[i])+" "
	else:
		i=i+1
print(c)
