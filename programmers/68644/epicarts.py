import itertools

def solution(numbers):
    combinations = itertools.combinations(numbers,2)
    answer = list(set([i+v for i,v in list(combinations)]))
    return sorted(answer)
