p = input()
q=0
r=0
for i in range(len(p)):
    if(p[i].isalpha() or p[i].isdigit()):
       q=q+1
    else:
        r=r+1
print(r)
