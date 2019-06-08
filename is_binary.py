#harini
S=input()
s=0
for i in range(0,len(S)):
	if(S[i]!='0' and S[i]!='1'):
		s=s+1
if(s>=1):
	print("no")
else:
	print("yes")
