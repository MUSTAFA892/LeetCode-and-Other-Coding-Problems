class Solution:
 
    def repeatedSubstringPattern(self, s: str) -> bool:
        updated_string = s + s

        return s in updated_string[1:-1]
        
"""        freq = Counter(s)
        ans = []
        
        for i  in freq.values():
            ans.append(i)

        set_ = set(ans)

        if len(set_) == 1:
            return True
        else:
            return False
"""