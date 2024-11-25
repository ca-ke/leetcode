import sys
from typing import List


class Solution:
    def leftProduct(self, nums: List[int]) -> List[int]:
        result = []
        count = 1
        for i in range(len(nums)):
            result.append(count)
            count *= nums[i]
        return result

    def rightProduct(self, nums: List[int]) -> List[int]:
        result = []
        count = 1
        for i in range(
            len(nums) - 1,
            -1,
            -1,
        ):
            result.append(count)
            count *= nums[i]
        return list(reversed(result))

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        leftProduct = self.leftProduct(nums)
        rightProduct = self.rightProduct(nums)

        for i in range(0, len(nums)):
            result.append(leftProduct[i] * rightProduct[i])
        return result


nums = list(map(lambda x: int(x), sys.argv[1].split(",")))
print(Solution().productExceptSelf(nums))
