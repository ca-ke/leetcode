import sys
from typing import List


class Solution:
    def canSplit(self, nums: List[int], penalty: int, maxOperations: int) -> bool:
        operations = 0
        for num in nums:
            if num > penalty:
                operations += (num - 1) // penalty
        return operations <= maxOperations

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            middle = (left + right) // 2
            if self.canSplit(nums, middle, maxOperations):
                right = middle
            else:
                left = middle + 1

        return left


nums = list(map(int, sys.argv[1].split(",")))
maxOperations = int(sys.argv[2])

print(Solution().minimumSize(nums, maxOperations))
