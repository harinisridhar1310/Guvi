#harini
N=int(input())
A=int(input())
D=int(input())
sum=0
for i in range(1,N+1):
	sum=sum+A
	A=A+D
print sum
