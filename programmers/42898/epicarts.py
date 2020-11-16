def solution(m, n, puddles):
    dp_arr = [[0] * (m + 1) for i in range(n + 1)] # dp 배열 0으로 초기화

    for puddle in puddles: # 웅덩이 초기화
        dp_arr[puddle[1]][puddle[0]] = -1
    dp_arr[1][1] = 1 # 가장 첫번쨰 값
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp_arr[i][j] == -1:# 웅덩이면 패스
                dp_arr[i][j] = 0
                continue
            elif i == 1 and j == 1: #첫번쨰열은 패스
                continue
            else:
                dp_arr[i][j] = (dp_arr[i - 1][j] + dp_arr[i][j - 1])
    return dp_arr[n][m] % 1000000007


# def is_out_of_array(m, n, x, y):  # 좌표 밖인지 체크
#     if x <= m and y <= n:
#         return True  # 좌표 안
#     return False  # 좌표 밖
#
#
# def is_puddles(puddles, x, y):
#     for puddle in puddles:  # 물에 있는가?
#         if puddle[0] == x and puddle[1] == y:
#             return False
#     return True  # 물에 없으면
#
#
# def dfs(current_x, current_y, m, n, depth, puddles):
#     global count, min_depth, min_count
#
#     # 만약 지금까지 구한 최소값보다 커진다면 굳이 갈필요없음
#     if min_depth < depth:
#         return
#
#     if current_x == m and current_y == n:  # 최종 좌표에 도착,
#         if depth == min_depth:  # 이미 최소값이 같다면?
#             min_count += 1  # 개수 추가
#             return
#
#         min_depth = depth  # 그렇지 않다면? 갱신 및 0으로 변환
#         min_count = 1
#         return
#
#     # 웅덩이가 없다면, dsf 로 접근.
#     for i in range(2):  # 아래, 오른쪽으로 이동
#         predict_x = current_x + direction[i][0]
#         predict_y = current_y + direction[i][1]
#         if is_out_of_array(m, n, predict_x, predict_y) and is_puddles(puddles, predict_x, predict_y):
#             dfs(predict_x, predict_y, m=m, n=n, depth=depth + 1, puddles=puddles)
# def solution(m, n, puddles):
#     dfs(current_x=1, current_y=1, m=m, n=n, depth=0, puddles=puddles)
#     return min_count
#

# 효율성 테스트 실패... ;;
direction = [[1, 0], [0, 1]]
min_depth = 999999999 #최소한으로 갈 수 있는 깊이
min_count = 0 #최소한으로 갈수 있는 depth의 개수
m = 3
n = 3
puddles = [[1, 2], [2, 1], [2, 2]]
print(solution(m, n, puddles))

m = 4
n = 5
puddles=[[1,2],[1,3],[1,4],[2,2],[3,2],[3,4],[4,4]]


print(solution(m, n, puddles))

m=3
n=1
puddles=[[2, 1]]


print(solution(m, n, puddles))
