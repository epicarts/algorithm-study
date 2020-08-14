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