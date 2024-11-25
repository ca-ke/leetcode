import sys
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return 0.0
        total = sum(nums[:k])
        maxTotal = total

        for i in range(0, len(nums) - k):
            total -= nums[i]
            total += nums[i + k]
            maxTotal = max(maxTotal, total)

        return maxTotal / k


nums = list(map(lambda x: int(x), sys.argv[1].split(",")))
k = int(sys.argv[2])

print(Solution().findMaxAverage(nums, k))
