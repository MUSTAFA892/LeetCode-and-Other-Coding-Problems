class Solution:
    def mirrorDistance(self, n: int) -> int:
        mirror = str(n)[::-1]
        return abs(n - int(mirror))