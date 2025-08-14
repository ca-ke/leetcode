from collections import deque


class Solution:
    def rotate_left_till_zero(self, nums: list[int]) -> list[int]:
        queue = deque(nums)
        while queue[0] != 0:
            queue.append(queue.popleft())
        return list(queue)


solution = Solution().rotate_left_till_zero([1, 2, 3, 4, 5, 0])
print(solution)
