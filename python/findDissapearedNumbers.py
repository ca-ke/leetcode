import sys
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numsSet = set(nums)
        expectedSet = set([value for value in range(1, len(nums) + 1)])
        return [value for value in (expectedSet - numsSet)]


nums = list(map(int, sys.argv[1].split(",")))
print(Solution().findDisappearedNumbers(nums))
