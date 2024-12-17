import heapq
from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        charCount = Counter(s)
        maxHeap = []
        result = []

        for char, count in charCount.items():
            heapq.heappush(maxHeap, (-ord(char), count))

        while maxHeap:
            value, count = heapq.heappop(maxHeap)
            currentChar = chr(-value)

            useCount = min(repeatLimit, count)
            result.append(currentChar * useCount)
            remainingCount = count - useCount

            if remainingCount > 0:
                if not maxHeap:
                    break

                nextValue, nextCount = heapq.heappop(maxHeap)
                nextChar = chr(-nextValue)
                result.append(nextChar)

                if nextCount - 1 > 0:
                    heapq.heappush(maxHeap, (nextValue, nextCount - 1))

                heapq.heappush(maxHeap, (value, remainingCount))

        return "".join(result)
