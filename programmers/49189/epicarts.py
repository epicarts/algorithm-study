from collections import deque

def search_next_nodes(vertex, current_node):
    result = []
    for v in vertex:
        if current_node in v:
            for i in v:
                if i != current_node:
                    result.append(i)
        vertex.remove(v)
    return result

def solution(n, vertex):
    visited = []  # 방문한 노드를 저장할 공간 생성
    queue = [1]  # 1부터 시작.

    while(queue):  # 큐가 없을때 까지
        next_nodes = []  # 주변 노드 찾기. 중복이 없어야함.

        for current_node in queue:  # 큐에 저장된 현재 노드 하나씩 꺼냄
            next_nodes.extend(search_next_nodes(vertex, current_node))

        visited.extend(queue)  # 방문한 노드 저장

        answer = len(queue)  # 정답.

        # 다음으로 탐색할 노드 찾기
        queue = []
        for i in set(next_nodes):
            if not i in visited:  # 방문한적이 없으면 다음 큐에 등록
                queue.append(i)

    return answer

vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6
print(solution(vertex, n))
