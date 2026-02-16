class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]

        if len(s) != 32:
            diff = 32 - len(s)
            
            addition = '0' * diff
            
            s = addition + str(s)
            
        conversion = s[::-1]
        return int(conversion,2)