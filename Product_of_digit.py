#harini
a=int(input())
prod=1
while(a>0):
	rem=a%10
	prod=prod*rem
	a=a//10
print(prod)
