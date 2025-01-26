class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = {'b':0,'a':0,'l':0,'o':0,'n':0}

        for i in text:
            if i in ans:
                ans[i] += 1
        ans['l'] //= 2
        ans['o'] //= 2
        
        return min(ans.values())