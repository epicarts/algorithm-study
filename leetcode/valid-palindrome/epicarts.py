import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        # 숫자, 소문자를 제외하고 전부 ''으로 치환
        s = re.sub('[^a-z0-9]','',s)

        return s == s[::-1]

s = "A man, a plan, a canal: Panama"

solution = Solution()
print(solution.isPalindrome(s))
