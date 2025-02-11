class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        dp = [1] * n  
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i:i + j - i] == s[j:j + j - i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return dp[0]
