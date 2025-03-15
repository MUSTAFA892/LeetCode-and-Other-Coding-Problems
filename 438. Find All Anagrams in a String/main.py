class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        indi = []
        len_s, len_p = len(s), len(p)

        if len_s < len_p:
            return indi

        else:
            p_count = Counter(p)
            window_count = Counter()
            
            for i in range(len_p):
                window_count[s[i]] += 1

            if window_count == p_count:
                indi.append(0)

            for i in range(len_p, len_s):
                window_count[s[i]] += 1
                window_count[s[i - len_p]] -= 1

                if window_count[s[i - len_p]] == 0:
                    del window_count[s[i - len_p]]

                if window_count == p_count:
                    indi.append(i - len_p + 1)

            return indi

"""        n = len(p)
        indi = []
        for i in range(0, len(s)):

            if sorted(s[i:n]) == sorted(p):
                indi.append(i)
            n += 1    

        return indi"""

"""        indi = []

        l , r = 0 , len(p)

        while r < len(s):
            if sorted(s[l:r]) == sorted(p):
                indi.append(l)
            l+=1
            r+=1

        return indi"""