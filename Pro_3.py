#harini
a,b=map(str,input().split())
z=abs(len(a)-len(b))
for i in range(len(a)):
        if len(b)==1 and b[i] in a:
            break
        if a[i]!=b[i]:
            z=z+1
print(z)
