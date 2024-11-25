import sys


class Solution:
    def isVowel(self, s: str) -> bool:
        return s in {"a", "e", "i", "o", "u"}

    def maxVowels(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        total = sum(1 if self.isVowel(i) else 0 for i in s[:k])
        maxTotal = total
        for i in range(1, len(s) - k + 1):
            if self.isVowel(s[i - 1]):
                total -= 1
            if self.isVowel(s[i + k - 1]):
                total += 1

            maxTotal = max(maxTotal, total)
        return maxTotal


print(Solution().maxVowels(sys.argv[1], int(sys.argv[2])))
