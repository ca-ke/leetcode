import sys
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        firstPointer, secondPointer, maxOperations = 0, len(nums) - 1, 0
        nums.sort()
        while firstPointer < secondPointer:
            if nums[firstPointer] + nums[secondPointer] == k:
                maxOperations += 1
                firstPointer += 1
                secondPointer -= 1
            elif nums[firstPointer] + nums[secondPointer] > k:
                secondPointer -= 1
            else:
                firstPointer += 1

        return maxOperations


nums = list(map(lambda x: int(x), sys.argv[1].split(",")))
k = int(sys.argv[2])
print(Solution().maxOperations(nums, k))
