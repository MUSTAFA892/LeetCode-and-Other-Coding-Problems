class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        first = 0
        last = len(s) - 1

        if len(s) == 1:
            return ''.join(s)

        while first <= last :
            if s[first].isalpha() and s[last].isalpha():
                s[first] , s[last] = s[last] , s[first]
                first += 1
                last -= 1
            
            if not s[first].isalpha():
                first += 1
            if not s[last].isalpha():
                last -= 1
        s = ''.join(s)

        return s