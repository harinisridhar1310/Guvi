#harini
d=int(input())
e=[]
for i in range(0,d):
    e.append(list(map(int,input().split())))
c=0
k=0
for i in range(0,d):
    for j in range(0,d):
        if e[i][j]==1:
            if i!=d-1 and e[i+1][j]==0:
                c=c+1
            if j!=d-1 and e[i][j+1]==0:
                c=c+1
            if i!=0 and e[i-1][j]==0:
                c=c+1
            if j!=0 and e[i][j-1]==0:
                c=c+1
            if i==0 and j==0 or i==d-1 and j==d-1  or i==0 and j==d-1 or i==d-1 and j==0 and c==2:
                k=k+1
            elif i==1 and j>0 and j<d-1 and c==3:
                k=k+1
            elif c==4:
                k=k+1
        c=0
                
print(k)
