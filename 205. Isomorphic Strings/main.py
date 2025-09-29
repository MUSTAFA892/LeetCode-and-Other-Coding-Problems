class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}

        for i ,j in zip(s,t):
            if i not in map_s:
                map_s[i] = j
            if j not in map_t:
                map_t[j] = i
            
            if map_s[i] != j or map_t[j] != i:
                return False
                
        return True