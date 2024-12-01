import sys
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True

        return False


nums = list(map(int, sys.argv[1].split(",")))
print(Solution().containsDuplicate(nums))
