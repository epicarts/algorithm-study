class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 왼쪽, 오른쪽으로 하나씩 확장
        def expand(left, right):
            # 왼쪽으로 확장을 충분히 했거나, 왼쪽 오른쪽이 같지 않으면
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # 찾은 문자열 리턴

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 0 ~ n - 1까지 반복. 우측으로 슬라이딩 2, 3 이동
        for i in range(0, len(s) - 1):
            odd = expand(i, i + 1)  # 홀수
            even = expand(i, i + 2)  # 짝수
            result = max(result, odd, even, key=len)
        return result


s = "abccccdd"
print(Solution().longestPalindrome(s))
