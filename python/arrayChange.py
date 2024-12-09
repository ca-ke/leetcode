from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mapping = {num: i for i, num in enumerate(nums)}
        for old, new in operations:
            index = mapping.pop(old)
            nums[index] = new
            mapping[new] = index

        return nums


nums = [1, 2, 4, 6]
operations = [[1, 3], [4, 7], [6, 1]]

print(Solution().arrayChange(nums, operations))
