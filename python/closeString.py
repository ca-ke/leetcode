import sys
from typing import List


class Solution:
    def getFrequencyVector(self, words: str) -> List[int]:
        result = [0] * 26
        for word in words:
            result[ord(word) - 97] += 1
        return result

    def closeString(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1Set = set(word1)
        word2Set = set(word2)

        if word1Set != word2Set:
            return False

        word1Frequency = self.getFrequencyVector(word1)
        word2Frequency = self.getFrequencyVector(word2)

        word1Frequency.sort()
        word2Frequency.sort()

        return word1Frequency == word2Frequency


print(Solution().closeString(sys.argv[1], sys.argv[2]))
