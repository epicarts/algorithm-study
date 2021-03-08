import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        word_counts = collections.Counter(s)

        # 전체 카운트에서 1또는 0만 남겨야함. 2 2 5 3 1 => 0 0 1 1 1
        for key, value in word_counts.items():
            result += (value // 2) * 2
            if value % 2 == 0:
                word_counts[key] = 0
            else:
                word_counts[key] = 1

        # palindrome center
        for value in word_counts.values():
            if value == 1:
                result += 1
                break

        return result


s = "ccc"
print(Solution().longestPalindrome(s))
