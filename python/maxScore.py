import sys


class Solution:
    def maxScore(self, s: str) -> int:
        totalZeroSum = 1 if int(s[0]) == 0 else 0
        totalOneSum = sum(1 if int(value) == 1 else 0 for value in s[1:])
        totalSum = totalZeroSum + totalOneSum
        for i in range(1, len(s) - 1):
            if int(s[i]) == 0:
                totalZeroSum += 1
            elif int(s[i]) == 1:
                totalOneSum -= 1
            total = totalZeroSum + totalOneSum
            totalSum = max(totalSum, total)
        return totalSum


print(Solution().maxScore(sys.argv[1]))
