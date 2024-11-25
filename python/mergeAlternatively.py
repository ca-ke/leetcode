class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        firstPointer = 0
        secondPointer = 0
        result = ""

        while firstPointer != len(word1) or secondPointer != len(word2):
            if firstPointer < len(word1):
                result += word1[firstPointer]
                firstPointer += 1
            if secondPointer < len(word2):
                result += word2[secondPointer]
                secondPointer += 1

        return result
