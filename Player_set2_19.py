#harini
a=int(input())
L=[]
b=0
for i in range(2,a+1):
  if(a%i)==0:
    L.append(i)
for i in L:
  b=0
  for j in range(1,i+1,1):
    if (i%j)==0:
      b=b+1
  if b==2:
    print (i,end=" ")
