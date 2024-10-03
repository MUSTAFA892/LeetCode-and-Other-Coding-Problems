class Solution:
    def reverseWords(self, s: str) -> str:
        final = " "
        a = s.split()
        for i in range(len(a) - 1,-1,-1):
            final += a[i] + " "
        return final.strip()