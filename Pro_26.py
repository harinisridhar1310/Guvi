#harini
num=int(input())
b=list(map(int,input().split()))
c=[]
k=1
for i in b:
  if i not in c:
    c.append(i)
for i in range(0,len(c)-1):
  if c[i]<c[i+1]:
    k+=1
print(k)
