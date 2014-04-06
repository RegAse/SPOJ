from math import sqrt
primes = [2]

for x in range(3,32000,2):
	isprim = True

	cap = sqrt(x) + 1

	for j in primes:
		if j >= cap:
			break
		if x % j == 0:
			isprim = False
			break
	if isprim:
		primes.append(x)
cases = int(input())
output = ""
for t in range(cases):

	if t > 0:
		output += "\n"
	m,n = input().split()
	m = int(m)
	n = int(n)
	cap = sqrt(n) + 1

	if m < 2:
		m = 2

	isprim = [True]*100001

	for d in primes:
		if d >= cap:
			break

		if d >= m:
			start = d*2
		else:
			start = m + ((d-m % d)%d)
		falseblock = [False] * len(isprim[start-m:n+1-m:d])
		isprim[start-m:n+1-m:d] = falseblock

	for k in range(m,n+1):
		if isprim[k-m] == True:
			output += str(k) + "\n"
print(output)