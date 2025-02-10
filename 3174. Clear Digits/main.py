class Solution:
    def clearDigits(self, s: str) -> str:
        while True:
            for i in range(1,len(s)):
                if s[i].isnumeric():
                    s = s[:i-1] + s[i+1:]
                    break
            else:
                break
            
        return s
