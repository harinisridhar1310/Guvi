#harini
n=int(input())
m=list(map(int,input().split(" ")))
l=[]
for i in range(len(m)):
    if(i==m[i]):
        l.append(i)
if l==[]:
   print("-1")
else:        
  l.sort()
  for i in l:
    print(i,end=" ")  
