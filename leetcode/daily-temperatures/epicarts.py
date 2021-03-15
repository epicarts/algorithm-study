from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0] * len(T)

        for i, v in enumerate(T):
            while stack and T[stack[-1]] < v: # 높은 온도가 오면
                last_index = stack.pop()
                result[last_index] = i - last_index #인덱스의 차로 결과를 저장
            stack.append(i)
        return result


T = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(T))
