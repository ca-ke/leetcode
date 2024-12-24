from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        edges1Tuple = tuple(tuple(edge) for edge in edges1)
        edges2Tuple = tuple(tuple(edge) for edge in edges2)

        d1 = self.treeDiameter(edges1Tuple)
        d2 = self.treeDiameter(edges2Tuple)

        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)

    def treeDiameter(self, edges: List[List[int]]) -> int:
        if edges in self.memo:
            return self.memo[edges]

        def dfs(i: int, fa: int, t: int):
            for j in g[i]:
                if j != fa:
                    dfs(j, i, t + 1)
            nonlocal ans, a
            if ans < t:
                ans = t
                a = i

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        ans = a = 0
        dfs(0, -1, 0)
        dfs(a, -1, 0)

        self.memo[edges] = ans
        return ans
