from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxScore = 0
        maxValuePlusIndex = values[0]

        for i in range(1, len(values)):
            maxScore = max(maxScore, values[i] - i + maxValuePlusIndex)
            maxValuePlusIndex = max(maxValuePlusIndex, values[i] + i)

        return maxScore
