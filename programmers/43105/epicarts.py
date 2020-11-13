def bfs(triangle, dp):
    for i, triangle_row in enumerate(triangle): # 맨 위층부터 맨 아래까지 순서대로 돌음.
        row = [] #한줄 넣을 예정
        if i == 0:#제일 상단.
            dp.append(triangle[0])
            continue
        else:
            for j, atomic in enumerate(triangle_row):
                if j == 0:#맨 좌측
                    row.append(dp[i - 1][0] + atomic)
                elif j == len(triangle_row) - 1: #맨 우측
                    row.append(dp[i - 1][len(triangle_row) - 2] + atomic)
                else: # 이전에 있던 값중 큰값을 가져옴.
                    row.append(max(dp[i - 1][j - 1], dp[i - 1][j]) + atomic)
            dp.append(row)
    return max(dp[i])

def solution(triangle):
    dp = []
    answer = bfs(triangle, dp)
    return answer

if __name__ == '__main__':
    a = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    solution(a)