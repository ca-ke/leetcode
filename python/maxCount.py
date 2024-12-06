import sys
from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bannedSet = set([value for value in banned if value <= maxSum])
        result = 0
        count = 0
        for i in range(1, n + 1):
            if result + i <= maxSum and i not in bannedSet:
                result += i
                count += 1
        return count


banned = list(map(int, sys.argv[1].split(",")))
n = int(sys.argv[2])
maxSum = int(sys.argv[3])

print(Solution().maxCount(banned, n, maxSum))
