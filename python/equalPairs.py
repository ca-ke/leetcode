from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = [tuple(row) for row in grid]
        cols = [tuple(col) for col in zip(*grid)]

        rowCount = Counter(rows)
        colCount = Counter(cols)

        result = 0
        for row in rowCount:
            if row in colCount:
                result += rowCount[row] * colCount[row]

        return result
