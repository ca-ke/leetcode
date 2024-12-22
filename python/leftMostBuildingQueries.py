from typing import List
from bisect import bisect_left
from math import inf


class BinaryIndexedTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [inf] * (size + 1)

    def update(self, index: int, value: int):
        while index <= self.size:
            self.tree[index] = min(self.tree[index], value)
            index += index & -index

    def query(self, index: int) -> int:
        minimum = inf
        while index:
            minimum = min(minimum, self.tree[index])
            index -= index & -index
        return -1 if minimum == inf else minimum


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        numHeights = len(heights)
        numQueries = len(queries)
        for i in range(numQueries):
            queries[i] = [
                min(queries[i]),
                max(queries[i]),
                i,
            ]  # Add index for original order

        queries.sort(key=lambda x: -x[1])  # Sort by descending `r`

        uniqueHeights = sorted(set(heights))  # Unique sorted heights
        binaryTree = BinaryIndexedTree(numHeights)
        currentIndex = numHeights - 1
        results = [-1] * numQueries

        for left, right, queryIndex in queries:
            while currentIndex > right:
                position = (
                    numHeights - bisect_left(uniqueHeights, heights[currentIndex]) + 1
                )
                binaryTree.update(position, currentIndex)
                currentIndex -= 1

            if left == right or heights[left] < heights[right]:
                results[queryIndex] = right
            else:
                position = numHeights - bisect_left(uniqueHeights, heights[left])
                results[queryIndex] = binaryTree.query(position)

        return results
