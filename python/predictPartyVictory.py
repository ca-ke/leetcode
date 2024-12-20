from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queueRadiant = deque()
        queueDire = deque()

        for index, senator in enumerate(senate):
            if senator == "R":
                queueRadiant.append(index)
            else:
                queueDire.append(index)

        while queueRadiant and queueDire:
            if queueRadiant[0] < queueDire[0]:
                queueRadiant.append(queueRadiant[0] + len(senate))
            else:
                queueDire.append(queueDire[0] + len(senate))
            queueRadiant.popleft()
            queueDire.popleft()

        return "Radiant" if queueRadiant else "Dire"


print(Solution().predictPartyVictory("s"))
