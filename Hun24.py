n,k=map(int,raw_input().split())
l=[int(i) for i in raw_input().split()]
c=0
for i in range(0,n):
	for j in range(i+1,n):
		if l[i]+l[j]==k:
			c+=1
if c!=0:
	print "YES"
else:
	print "NO"
