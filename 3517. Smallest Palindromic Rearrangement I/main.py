class Solution:
    def smallestPalindrome(self, s: str) -> str:
        new_s = ""

        n = len(s)

        map_ = {}

        for i in s:
            if i not in map_:
                map_[i] = 1
            else:
                map_[i] += 1

        if n % 2 == 0: 
            left_half = s[0:(n//2)]
            left_half_vals = ''.join(sorted(left_half))
            new_s += left_half_vals
            new_s += left_half_vals[::-1]
            
        else:
            sample_s = ""
            odd_val = ''
            for i, j in map_.items():
                sample_s += i * (j//2)
                if j % 2 != 0:
                    odd_val += i
            left_half_sorted = ''.join(sorted(sample_s))
            new_s += left_half_sorted + odd_val + left_half_sorted[::-1]

        return new_s
            
            