#harini
a=int(input())
b=list(map(int,input().split()))
l=[]
f=''
for i in range(0,len(b)):
	l.append(b[i])
	f+=str(max(l))+' '
print(f)
