class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        dp = [1] * len(strs[0])

        for j in range(len(strs[0])):
            for i in range(j):
                valid = True
                for r in range(len(strs)):
                    if strs[r][i] > strs[r][j]:
                        valid = False
                        break
                if valid:
                    dp[j] = max(dp[j], dp[i] + 1)

        return len(strs[0]) - max(dp)
