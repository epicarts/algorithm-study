def solution(n, lost, reserve):
    count = 0

    for lo in lost:  # 잃어버린 인원체크

        # 자기자신이 여벌의 옷을 가지고 있는가?
        if lo in reserve:
            reserve.remove(lo)
            continue

        # 앞 사람이 여벌의 옷을 가지고 있는가 ?
        if (lo - 1) in reserve:
            reserve.remove(lo - 1)
            continue

        # 뒤 사람이 여벌의 옷을 가지고 있는가 ?
        if (lo + 1) in reserve:
            reserve.remove(lo + 1)
            continue

        count += 1
    return n - count

def solution2(n, lost, reserve):
    arr = [1] * n
    for l in lost:
        arr[l - 1] -= 1
    for r in reserve:
        arr[r - 1] += 1

    for i in range(n - 1):
        if arr[i] == 0 and arr[i + 1] == 2:
            arr[i] = 1
            arr[i + 1] = 1
        if arr[i] == 2 and arr[i + 1] == 0:
            arr[i] = 1
            arr[i + 1] = 1
    return n - arr.count(0)


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
print(solution2(n, lost, reserve))