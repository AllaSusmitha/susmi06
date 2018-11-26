n,k=map(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
c=0
for i in range(0,n):
	for j in range(i+1,n):
		if l[x]+l[y]==k:
			c+=1
if c!=0:
	print "YES"
else:
	print "NO"
