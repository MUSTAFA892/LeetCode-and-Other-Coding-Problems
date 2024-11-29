class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        elif s1 == s2:
            return True

        else:
            Not_Equal = []
            for i in range(len(s1)):
                if s1[i] == s2[i]:
                    continue
                else:
                    Not_Equal.append(i)
        
        if len(Not_Equal) == 2:
            i , j = Not_Equal
            if s1[i] == s2[j] and s1[j] == s2[i]:
                return True
        
        return False
