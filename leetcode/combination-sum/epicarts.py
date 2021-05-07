from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        # 중복가능
        def dfs(c_sum, start, path):
            # print(path)
            if target < c_sum: # 타겟보다 커지면
                return
            # 정답이 나올때마다 추가
            if target == c_sum:
                result.append(path)
                return

            # 자가자신 외에 중복되지 않은 조합.
            for i in range(start, len(candidates)):
                # 자기자신 포함이기 때문에 'i'임. 자기자신이 아닐경우 i + 1을 넣어야함.
                dfs(c_sum + candidates[i], i, path + [candidates[i]])

            # 순열,
            # for candidate in candidates:
            #     dfs(candidate + c_sum,  path + [candidate]) # 다음 수 전달

        dfs(0, 0, [])
        return result


candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
