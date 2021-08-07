

import sys
sys.setrecursionlimit(10**6)

max_number = 10000
arr = (max_number + 1) * [0] # 전부 셀프 넘버로 초기화


def dn(n):
	if (n >= max_number):
		return
	dnum = n
	while(1):
		dnum += n % 10
		n = int(n / 10)
		if (n == 0):
			break
	if (dnum < max_number and arr[dnum] == 0):
		arr[dnum] = 1
	return dn(dnum)


for i in range(1, max_number):
	if (arr[i] != 1):
		dn(i)

for i in range(1, max_number):
	if (arr[i] == 0):
		print(i)