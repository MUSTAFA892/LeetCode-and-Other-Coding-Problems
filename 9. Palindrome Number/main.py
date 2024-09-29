class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        return str(x) == a[::-1]