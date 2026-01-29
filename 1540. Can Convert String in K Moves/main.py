class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        shifts = []
        count = {}
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):

            if s[i] != t[i]:
                distance = (ord(t[i]) - ord(s[i]) + 26) % 26

                times_used = count.get(distance, 0)   
                shift = distance + 26 * times_used    

                count[distance] = times_used + 1     
              
                if shift > k:
                    return False
                    
        return True