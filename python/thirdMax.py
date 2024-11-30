import sys
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)

        return nums[0] if len(nums) < 3 else nums[2]


nums = list(map(int, sys.argv[1].split(",")))
print(Solution().thirdMax(nums))
