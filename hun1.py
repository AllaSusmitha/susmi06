a=int(input())
l=[int(x) for x in raw_input().split()]
li=[]
for i in range(0,a):
	for j in range(i+1,a):
		if(l[i]==l[j] and l[i] not in li):
			li.append(l[i])
if l[i] in li:
	li.sort()
	print " ".join(map(str,li))
else:
	print ("unique")
