def solution(prices):
    answer = [0] * len(prices)

    for i, price in enumerate(prices): #첫번쨰 가격부터 마지막 가격까지..
        second = 0 # 0초부터 계산.
        for after_price in prices[i+1:]:
            second = 1 + second
            #i + 1번빼 부터 비교를 했을떄, 즉 다음거부터 비교를 했을때 
            answer[i] = second
            if after_price < price:
                break #값이 작은게 나오면, 중간에 리턴
    return answer


from collections import deque

def solution(prices):
    answer = deque()
    prices = deque(prices)

    while(prices):
        count = 0
        p = prices.popleft() # n만큼 컬리던 것을 O(1) 로 변환
        for i in prices:
            count+=1
            if i < p :
                break

        answer.append(count)
    return list(answer)
