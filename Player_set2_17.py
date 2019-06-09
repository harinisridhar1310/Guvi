#harini
l,r=input().split()
l=int(l)
r=int(r)
list=[]
for i in range(1,1000):
	if i%l==0 and i%r==0:
		list.append(i)
print(min(list))
