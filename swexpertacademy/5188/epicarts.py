import sys

sys.stdin = open("input.txt", "r")

def dfs(x, y, node_result):
    global answer

    node_result += arr[x][y]

    if answer < node_result:
        # 원래 구한 기존의 값보다 크면 더 볼 필요도 없음.
        return

    if y == arr_size-1 and x == arr_size-1: # 마지막 노드 도착시 빠져나가면 됨.
        answer = node_result #마지막 노드이므로 정답임!
        return

    for direction in range(2):
        new_y = y + dd[direction] # 아래부터 이동 dd[0] 은 1 dd[1] 은 0
        new_x = x + dr[direction] # 오른쪽 이동은 두번째부터 dr[0]: 0 , dr[1]: 1
        if new_y < arr_size and new_x < arr_size: # y 와 x 는 밖으로 나가면 안됨
            dfs(new_x, new_y, node_result)



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

dr = [0, 1] # 1열 증가 => 오른쪽으로 한칸 right
dd = [1, 0] # 1행 증가 => 아래로 한칸 down

for test_case in range(1, T + 1):
    arr_size = int(input())
    arr = []

    for i in range(0, arr_size):
        arr.append(list(map(int, input().split())))

    answer = 99999999999

    dfs(0, 0, 0)
    print('#{} {}'.format(test_case, answer))
