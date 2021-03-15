import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        stack = []

        for char in s:
            counter[char] -= 1
            if char in stack: # 이미 스택에 들어가 있다면 생략.
                continue
            # 1. 스택이 비어있지 않아야 하고, 스택에 마지막 값이 더 작고, 1개 이상의 값이 뒤에 있다면. => 기존 값을 스택에서 제거 (while)
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
        return ''.join(stack)



s = "cbacdcbc"
print(Solution().removeDuplicateLetters(s))
