def solution(people, limit):
    people.sort()
    start_idx = 0
    end_idx = len(people) - 1
    count = 0
    
    while (start_idx <= end_idx): #서로 크로스 되면 종료
        if people[start_idx] + people[end_idx] <= limit: # 둘이 같이 타는 경우
            start_idx += 1
        count += 1
        end_idx -= 1
    return count

