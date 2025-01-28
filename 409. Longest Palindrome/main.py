class Solution:
    def longestPalindrome(self, s: str) -> int:
        center_added = False
        frequency = Counter(s)
        ans = ""

        for value , count in frequency.items():
            if count % 2 == 0:
                ans += value * count

            else:
                ans += value * (count-1)
                if not center_added:
                    ans += value
                    center_added = True
        
        return len(ans)