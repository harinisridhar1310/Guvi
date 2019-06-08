#harini
a,b=input().split()
x=int(a)
y=int(b)
c=0
s=list(map(int,input().split()))
for i in range(len(s)):
    if(s[i]==y):
        c+=1
print(c)
