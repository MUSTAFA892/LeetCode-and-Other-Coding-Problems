class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        r =  0

        while r < len(s):

            s[r:r+k] = reversed(s[r:r+k])
            r += 2 * k


        return ''.join()