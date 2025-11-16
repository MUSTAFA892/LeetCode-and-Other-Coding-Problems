class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7 
        str_count = 0
        l ,r = 0 , 0 

        while r < len(s):
            if s[l] == '0' and s[r] == '0':
                l += 1
                r = l
            
            elif s[l] == '1' and s[r] == '1':
                r += 1
            
            elif s[r] == '0':
                str_count +=(r-l) * (r - l + 1) // 2
                str_count %= MOD
                l = r

        if l < r:
            str_count += (r-l) * ((r-l)+1) // 2
            str_count %= MOD
            

        return str_count
            