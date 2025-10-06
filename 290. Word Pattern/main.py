class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_map = {}
        pattern_map = {}
        s = s.split()
        flag = True

        if len(s) != len(pattern):
            return False
            
        for i in range(len(s)):
            if pattern[i] not in pattern_map:
                pattern_map[pattern[i]] = s[i] 
            if s[i] not in s_map and pattern_map[pattern[i]] == s[i]:
                s_map[s[i]] = pattern[i]
                
            elif pattern_map[pattern[i]] != s[i] or s_map[s[i]] != pattern[i] :
                flag = False
                break
        
        return flag
