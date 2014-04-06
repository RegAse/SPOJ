cases = int(input())
output = ""
li = []
for x in range(cases):
	l = int(input())
	total = 0
	for x1 in range(1,l):
		if l % x1 == 0 :
			total += x1
	output += str(total) + "\n"
print(output)