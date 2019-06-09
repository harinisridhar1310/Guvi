#harini
n,k=input().split()
k=int(k)
d=list(map(int,input().split()))
d.sort()
print(d[k-1])
