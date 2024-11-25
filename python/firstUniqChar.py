import sys


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        candidate = ""
        result = -1
        for letter in s:
            if counter.get(letter) is not None:
                counter[letter] += 1
            else:
                counter[letter] = 1

        for i, (k, v) in enumerate(counter.items()):
            if v == 1:
                candidate = k
                break

        for i, letter in enumerate(s):
            if candidate == "":
                break
            elif candidate == letter:
                result = i
        return result


print(Solution().firstUniqChar(sys.argv[1]))
