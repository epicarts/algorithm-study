def solution(s):
    low_s = s.lower()
    if low_s.count('p') is low_s.count('y'):
        return True
    return False
