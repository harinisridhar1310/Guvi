#harini
p = input()
q=0
g=0
r=0
for i in range(len(p)):
    if(p[i].isalpha()):
       q=q+1
    elif(p[i].isdigit()):
      	g=g+1
    else:
        r=r+1
if(q>0 and g>0):
	print("Yes")
else:
	print("No")
