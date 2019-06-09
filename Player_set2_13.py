#harini
a=int(input())
sum=0
while(a!=0):
	rem=a%10
	sum=sum+rem*rem
	a=a//10
print(sum)
