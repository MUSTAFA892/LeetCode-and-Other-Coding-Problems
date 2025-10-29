class Solution:
    def smallestNumber(self, n: int) -> int:
        for i in range(n+1):
            num = (2**i) - 1
            if num >= n:
                return num