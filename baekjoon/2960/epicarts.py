import sys


def solution(N, K):
	sieve = [0] * (N + 1)
	
	for i in range(2, N + 1): # 2 ~ N 
		for j in range(i, N + 1, i): # i 부터 N까지 i의 배수로
			if sieve[j] != 1:
				sieve[j] = 1
				K-=1
			if K == 0:
				return j



N, K = map(int, sys.stdin.readline().split())
print(solution(N, K))
