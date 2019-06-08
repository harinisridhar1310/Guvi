#harini
a=input()
c=0
s=['a','e','i','o','u']
for i in range(0,len(a)):
	if a[i] in s:
		c=c+1
if c>0:
	print("yes")
else:
	print("no")
