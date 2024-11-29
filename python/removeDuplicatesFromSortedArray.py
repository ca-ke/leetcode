import sys
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            if result == 0 or nums[i] != nums[result - 1]:
                nums[result] = nums[i]
                result += 1

        return result


nums = list(map(int, sys.argv[1].split(",")))
print(Solution().removeDuplicates(nums))
