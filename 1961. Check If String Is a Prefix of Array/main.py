class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""
        for i in words:
            prefix += i
            if prefix == s:
                return True
            if len(prefix) > len(s):
                break
        
        return False
