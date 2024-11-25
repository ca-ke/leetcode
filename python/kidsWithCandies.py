import sys
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        biggestCandyNumber = 0

        for candy in candies:
            if candy > biggestCandyNumber:
                biggestCandyNumber = candy

        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= biggestCandyNumber)

        return result


candies = list(map(lambda x: int(x), sys.argv[1].split(",")))
extraCandies = int(sys.argv[2])

print(Solution().kidsWithCandies(candies=candies, extraCandies=extraCandies))
