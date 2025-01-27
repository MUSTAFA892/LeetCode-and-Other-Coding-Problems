class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [float('inf')] * (len(s) + 1)
        dp[0] = 0


        for i in range(1,len(s) + 1):
            for j in range(i):
                if s[j:i] in dictionary:
                    dp[i] = min(dp[i],dp[j])
            
            dp[i] = min(dp[i], dp[i-1]+1)
        
        return dp[len(s)]