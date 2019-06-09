#harini
a=input()
mid=len(a)//2
if mid%2==0:
	print(a[:mid]+"*"+a[mid+1:])
else:
	print(a[:mid-1]+"**"+a[mid+1:])
