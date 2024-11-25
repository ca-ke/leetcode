import sys
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j, count = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[j] = nums[i]
                j += 1

        print(nums)
        return j


nums = list(map(lambda x: int(x), sys.argv[1].split(",")))
print(Solution().removeDuplicates(nums))
