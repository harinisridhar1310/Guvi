#harini
f=input()
f=f.split(" ")
g=list(f[0])
h=list(f[1])
k=int(f[2])
c=0
for i in range(0,len(g)):
          if(g[i]!=h[i]):
                 c=c+1
if(c==k):
     print("yes")
else:
     print("no")
