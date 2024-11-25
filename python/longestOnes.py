import sys
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = -1

        while right < len(nums) - 1:
            right += 1
            if nums[right] == 0:
                k -= 1
            if k < 0:
                left += 1
                if nums[left] == 0:
                    k += 1
        return right - left


nums = list(map(lambda x: int(x), sys.argv[1].split(",")))
k = int(sys.argv[2])
print(Solution().longestOnes(nums, k))
