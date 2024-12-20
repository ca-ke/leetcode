from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])

        level = 0

        while queue:
            currentLevelNodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if level % 2 == 1:
                    currentLevelNodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if currentLevelNodes:
                left, right = 0, len(currentLevelNodes) - 1
                while left < right:
                    currentLevelNodes[left].val, currentLevelNodes[right].val = (
                        currentLevelNodes[right].val,
                        currentLevelNodes[left].val,
                    )
                    left += 1
                    right -= 1
            level += 1
        return root
