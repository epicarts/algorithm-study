def is_out_of_array(m, n, x, y):  # 좌표 밖인지 체크
    if x <= m and y <= n:
        return True  # 좌표 안
    return False  # 좌표 밖


def is_puddles(puddles, x, y):
    for puddle in puddles:  # 물에 있는가?
        if puddle[0] == x and puddle[1] == y:
            return False
    return True  # 물에 없으면


def dfs(current_x, current_y, m, n, depth, puddles):
    global count, min_depth, min_count

    # 만약 지금까지 구한 최소값보다 커진다면 굳이 갈필요없음
    if min_depth < depth:
        return

    if current_x == m and current_y == n:  # 최종 좌표에 도착,
        if depth == min_depth:  # 이미 최소값이 같다면?
            min_count += 1  # 개수 추가
            return

        min_depth = depth  # 그렇지 않다면? 갱신 및 0으로 변환
        min_count = 1
        return

    # 웅덩이가 없다면, dsf 로 접근.
    for i in range(2):  # 아래, 오른쪽으로 이동
        predict_x = current_x + direction[i][0]
        predict_y = current_y + direction[i][1]
        if is_out_of_array(m, n, predict_x, predict_y) and is_puddles(puddles, predict_x, predict_y):
            dfs(predict_x, predict_y, m=m, n=n, depth=depth + 1, puddles=puddles)
def solution(m, n, puddles):
    dfs(current_x=1, current_y=1, m=m, n=n, depth=0, puddles=puddles)
    return min_count
# 효율성 테스트 실패... ;;

direction = [[1, 0], [0, 1]]
min_depth = 999999999 #최소한으로 갈 수 있는 깊이
min_count = 0 #최소한으로 갈수 있는 depth의 개수
m = 4
n = 3
puddles = [[2, 2]]
solution(m, n, puddles)
