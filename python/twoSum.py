import sys
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        result = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complements.get(complement) is not None:
                result = [complements[complement], i]
                break
            complements[nums[i]] = i
        return result


nums = list(map(int, sys.argv[1].split(",")))
target = int(sys.argv[2])

print(Solution().twoSum(nums, target))
