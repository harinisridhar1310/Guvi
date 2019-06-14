#harini
a,b=map(int,input().split())
l1=[]
c=0
for i in range(1,b+1):
    sq=i*i
    if(sq<=b):
        l1.append(i*i)
    else:
        break
for j in range(a,b+1):
    if(j in l1):
        c+=1
print(c)
