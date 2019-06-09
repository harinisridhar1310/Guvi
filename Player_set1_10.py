#harini
h,s=input().split()
u=0
for i in range(len(h)):
    if h[i]!=s[i]:
        u+=1
            
if u==1:
    print("yes")
else:
    print("no")
