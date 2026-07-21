class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = 0
        odd = 0

        for i in range((n*2)+1):
            if i % 2 == 0:
                even += i
            else:
                odd += i

        return math.gcd(even,odd)