#harini
n=int(input())
s=input()
d=list(s[::-1])
v=[]
for i in range(n):
	if(d[i] in ('a','e','i','o','u')):
		v.append(d[i])
	else:
		print(d[i],end='')
