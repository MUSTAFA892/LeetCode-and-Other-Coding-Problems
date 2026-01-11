class Solution:
    def hammingWeight(self, n: int) -> int:
        val = bin(n)[2:]
        return str(val).count('1')