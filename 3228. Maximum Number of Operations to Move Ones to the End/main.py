class Solution:
    def maxOperations(self, s: str) -> int:
        ones_count = 0
        total_ops = 0

        for i in range(len(s)):
            if s[i] == '1':
                ones_count += 1

            elif s[i] == '0' and i > 0 and s[i-1] == '1':
                total_ops += ones_count
        
        return total_ops