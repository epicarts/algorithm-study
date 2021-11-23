from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(i: int, j: int):
            if i < 0 or len(grid) <= i or j < 0 or len(grid[0]) <= j or grid[i][j] != '1':
                return
            grid[i][j] = '#'

            # 4방향으로 탐색
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(Solution().numIslands(grid))
