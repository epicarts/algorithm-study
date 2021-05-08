import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []

        # 그래프 로 바꾼다. 앞은 키, 뒤는 벨류
        graph = collections.defaultdict(list)

        # 문제의 조건에 맞게 정렬
        for a, b in sorted(tickets):
            graph[a].append(b)

        # 갈 수 있는 최단 그래프
        def dfs(path):
            while graph[path]:
                dfs(graph[path].pop(0))
            result.append(path)

        dfs("JFK")

        return result[::-1]


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(Solution().findItinerary(tickets))