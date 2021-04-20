import sys

# 입력 처리 / 공통부분
N,M = map(int, sys.stdin.readline().split()) # 카드의 개수
cards = [int(i) for i in sys.stdin.readline().split()] # 카드. 정렬이 보장되어 있지 않음.

# 3중 반복문 / 시간 120ms
def solution_2(cards: list[int], target: int) -> int:
	answer = 0
	for i in range(0, len(cards) - 2): # 0 ~ n -2 맨끝 두번쨰 까지
		for j in range(i + 1, len(cards) - 1): # i 다음 수부터 바로 맨끝 전까지
			for k in range(j + 1, len(cards)): # j 바로 다음 수 부터 바로 맨끝 까지
					candidate = cards[i]+cards[j]+cards[k]
					if candidate <= M:
						answer = max(answer, candidate)
	return answer
print(solution_2(cards, M))

# 5 6 7 8 9 
# 출력 5 6 7
# 출력 5 6 8
# 출력 5 6 9
# 출력 5 7 8
# 출력 5 7 9
# 출력 5 8 9
# 출력 6 7 8
# 출력 6 7 9
# 출력 6 8 9
# 출력 7 8 9


# 2중 반복문 / 투포인터 / 시간 68ms
def solution_1(cards: list[int], target: int) -> int:
	answer = 0
	cards.sort() # 투포인터 사용시 정렬 필수
	for i in range(0, len(cards) - 2): # 0 ~ n -2 맨끝 두번쨰 까지
		left, right = i + 1, len(cards) - 1
		while left != right: # 둘이 만날떄까지 반복
			candidate = cards[left] + cards[right] + cards[i]
			if candidate < target: # 더 작으면 숫자를 키워야함.
				left += 1
				answer = max(answer, candidate) # 작은 경우만 넣어야함.
			elif candidate > target: # 타겟보다 크면 숫자를 줄여야함.
				right -= 1
			elif candidate == target:
				return candidate # 정답이면 종료
	return answer

print(solution_1(cards, M))
