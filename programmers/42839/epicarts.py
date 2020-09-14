import itertools
import math

def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num%i == 0:
                return False
    return True

def solution(numbers):
    answer = 0
    cases = []
    
    for i in range(len(numbers)):
        cases.extend(list(itertools.permutations(numbers, i + 1)))
        
    str_list_cases = [int("".join(list(case))) for case in cases]
    unique_str_cases = set(str_list_cases)
    
    for str_case in unique_str_cases:
        int_case = int(str_case)
        if is_prime(int_case):
            answer += 1
    return answer