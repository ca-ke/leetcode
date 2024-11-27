import sys
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        subarraySums = {0: 1}
        prefixSum = 0
        for num in nums:
            prefixSum += num
            count += subarraySums.get(prefixSum - k, 0)
            subarraySums[prefixSum] = subarraySums.get(prefixSum, 0) + 1
        return count


nums = list(map(int, sys.argv[1].split(",")))
k = int(sys.argv[2])
print(Solution().subarraySum(nums, k))
