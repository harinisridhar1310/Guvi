#harini
a=input()
c=0
for i in a:
	if (i.isnumeric())==False:
		c=c+1
if(c>0):
	print("no")
else:
	print("yes")
