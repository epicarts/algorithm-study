"""
def solution(prices):
    answer = []
    for i in range(len(prices)):
        check = 0;
        price = prices.pop(0)
        for j in prices:
            if(price < j or price == j):
                check += 1
            elif(len(prices)!=0):
                check += 1
                break
        answer.append(check)
    return answer
"""

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    return answer