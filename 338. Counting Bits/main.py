class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            value = bin(i)[2:]
            ans.append(value.count('1'))

        return ans