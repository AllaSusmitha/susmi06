a,b=map(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
c=0
for x in range(0,a):
	for y in range(x+1,a):
		if l[x]+l[y]==b:
			c+=1
if c!=0:
	print "YES"
else:
	print "NO"
