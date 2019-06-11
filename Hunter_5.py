#harini
m=input()
j=1
for i in range(len(m)-1):
    s=m[i]+m[i+1]
    p=int(s)
    if p<=26 and m[i]!="0":
        j+=1
if j==3:
    print(j)
else:
    print(j+(j-1)//2)
