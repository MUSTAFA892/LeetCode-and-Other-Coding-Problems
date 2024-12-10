class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        map_ = {}
        max_ = -1
        for i in range(n):
            for j in range(i,n):
                substring = s[i:j + 1]
                unique = set(substring)
                if len(unique) == 1:
                    map_[substring] = map_.get(substring, 0) + 1
        for keys , values in map_.items():
            if values >= 3:
                max_ = max(max_, len(keys))
        return max_