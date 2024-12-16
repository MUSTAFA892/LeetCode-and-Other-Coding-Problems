class Solution:
    def isBalanced(self, num: str) -> bool:
        Even = []
        Odd = []
        for i in range(len(num)):
            if i % 2 == 0:
                Even.append(int(num[i]))
            else:
                Odd.append(int(num[i]))
        return sum(Even) == sum(Odd)
