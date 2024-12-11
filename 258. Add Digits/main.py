class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            result = []
            for i in str(num):
                result.append(int(i))
            num = sum(result)
        return num