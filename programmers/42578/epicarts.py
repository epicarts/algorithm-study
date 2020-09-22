import collections

def solution(clothes):
    result = 1
    z = collections.Counter([i[1] for i in clothes])
    for i in z.values():
        result = result * (i+1)
    
    return result - 1
