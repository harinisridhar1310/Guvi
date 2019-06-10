#harini
a=int(input())
L=[]
x=0
z=0
for i in range(a):
    b=input()
    L.append(b)
for i in L:
    for y in i:
        x+=ord(y)
    if x==612:
        z+=1
    x=0
print(z)
