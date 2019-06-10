#harini
a1,b1=map(int,input().split())
input()
Num=list(map(int,input().split()))
k=list(map(int,input().split()))
s=''
for i in k:
  Num.append(i)
  s+=str(max(Num))+' '
print(s[:-1])
