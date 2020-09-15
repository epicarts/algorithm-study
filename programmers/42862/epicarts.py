def solution(n, lost, reserve):
    count = 0
    losted = list(set(lost) - set(reserve))
    reserved = list(set(reserve) - set(lost))
    for lo in losted:  # 잃어버린 인원체크

        # 앞 사람이 여벌의 옷을 가지고 있는가 ?
        if (lo - 1) in reserved:
            reserved.remove(lo - 1)
            continue

        # 뒤 사람이 여벌의 옷을 가지고 있는가 ?
        if (lo + 1) in reserved:
            reserved.remove(lo + 1)
            continue
        count += 1
    return n - count


lost = [2, 5]
reserve = [3, 4]
n = 5

n = 9
lost = [1, 2, 3, 4, 7]
reserve = [1, 2, 3, 4, 9]
# answer = 8

n = 100
lost = [27, 90, 41]
reserve = [28, 91, 42]
# answer = 97
# 내 정답: 100

print(solution(n, lost, reserve))
