def FindPrimeBetween(start,end):
	lis = []
	for d in range(start,end + 1):
		k = True
		if d < 2:
			k = False
		else:
			for l in range(2,int(d/2) + 1):
				if d % l == 0:
					k = False
					break
		if k == True:
			lis.append(d)
	return lis
cases = int(input())
li = []
for case in range(cases):
	x = [int(x) for x in input().split()]
	li.append(x[0])
	li.append(x[1])
for k in range(0,len(li),2):
	hk = FindPrimeBetween(li[k],li[k + 1])
	for r in hk:
		print(r)
	print()