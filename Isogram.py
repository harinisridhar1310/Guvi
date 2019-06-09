#harini
x=input()
count=0
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if(x[i]==x[j]):
            count=count+1
if count==0:
    print("Yes")
else:
    print("No")
