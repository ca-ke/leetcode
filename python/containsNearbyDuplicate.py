import sys
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        seenNumbers = {}

        for i, num in enumerate(nums):
            if num in seenNumbers and i - seenNumbers[num] <= k:
                return True

            seenNumbers[num] = i
        return False


nums = list(map(lambda x: int(x), sys.argv[1].split(",")))
k = int(sys.argv[2])

print(Solution().containsNearbyDuplicate(nums, k))
