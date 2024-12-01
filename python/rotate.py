import sys
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()

        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


nums = list(map(int, sys.argv[1].split(",")))
k = int(sys.argv[2])

print(Solution().rotate(nums, k))
