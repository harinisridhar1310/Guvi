#harini
n1,m1=map(int,input().split())
l=[]
ui=0
for i in range(n1):
    l.append(list(map(int,input().split())))   
for i in range(n1):
    for j in range(m1-1):
        for k in range(j+1,m1+1):
            if l[i][j:k]==[1]*len(l[i][j:k]):
                 if all(l[p+i][j:k]==[1]*len(l[p+i][j:k]) for p in range(len(l[i][j:k])-1)):
                     if len(l[i][j:k])>ui:
                        ui=len(l[i][j:k])
if len(l)==1 and len(l[0])==1 and l[0][0]==1:
    print(1)
for i in range(ui):
    print(*[1]*ui) 
