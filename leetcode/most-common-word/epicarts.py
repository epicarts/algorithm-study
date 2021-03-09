import re
from typing import List
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub('[^\w]', ' ', paragraph).lower().split()
        words = [word for word in words if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))
