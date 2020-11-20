def dfs(computers, node_idx, n, visited):
    visited[node_idx] = True  # 방문 도장

    for k, com in enumerate(computers[node_idx]):  # 노드
        if visited[k] is False and node_idx != k and com == 1:
            # 방문한 적이 없고, 자기자신이 아니고, 1인 노드를 방문
            dfs(computers, k, n, visited)


def solution(n, computers):
    count = 0
    visited = [False] * n  # 방문 노드

    for node_idx, computer in enumerate(computers):
        if visited[node_idx] is False:
            dfs(computers, node_idx, n, visited)
            count += 1

    return count
