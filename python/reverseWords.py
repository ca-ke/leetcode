import sys


class Solution:
    def splitInWords(self, s: str) -> list:
        result = []
        word = ""
        for letter in s:
            if letter != " ":
                word += letter
            else:
                if word != "":
                    print(word)
                    result.append(word)
                word = ""
        if word:
            result.append(word)
        return result

    def reverse(self, array: list) -> list:
        result = []
        for i in range(0, len(array)):
            result.append(array[len(array) - i - 1])
        return result

    def reverseWords(self, s: str) -> str:
        splitedWords = self.splitInWords(s=s)
        result = self.reverse(array=splitedWords)
        return " ".join(result)


print(Solution().reverseWords(s=sys.argv[1]))
