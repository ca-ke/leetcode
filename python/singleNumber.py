import sys
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seenElements = {}
        pos = 0

        for i in range(len(nums)):
            if seenElements.get(nums[i]) is not None:
                seenElements[nums[i]] += 1
            else:
                seenElements[nums[i]] = 0

        for _, (k, v) in enumerate(seenElements.items()):
            if v == 0:
                pos = k
        return pos


nums = list(map(int, sys.argv[1].split(",")))
print(Solution().singleNumber(nums))
