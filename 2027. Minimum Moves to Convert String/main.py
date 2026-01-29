class Solution:
    def minimumMoves(self, s: str) -> int:
        count = 0
        skip = 0
        for i in range(len(s)):
            if s[i] == 'X' and skip == 0:
                count += 1
                skip = 2
                
            elif skip > 0:
                skip -= 1
                
        return count