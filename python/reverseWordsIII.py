import sys


class Solution:
    def reverseWord(self, s: str) -> str:
        letters = list(s)
        firstPointer, endPointer = 0, len(letters) - 1

        while firstPointer < endPointer:
            letters[firstPointer], letters[endPointer] = (
                letters[endPointer],
                letters[firstPointer],
            )
            firstPointer += 1
            endPointer -= 1
        return "".join(letters)

    def reverseWords(self, s: str) -> str:
        splittedWords = s.split(" ")
        for i in range(len(splittedWords)):
            splittedWords[i] = self.reverseWord(splittedWords[i])
        return " ".join(splittedWords)


print(Solution().reverseWords(sys.argv[1]))
