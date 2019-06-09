#harini
x=input()
l=[]
m=[]
for i in range(0,len(x)):
    if(i%2==0):
        l.append(x[i])
    else:
        m.append(x[i])
n="".join(map(str,l))
print(n,end=' ')
print("".join(map(str,m)))
