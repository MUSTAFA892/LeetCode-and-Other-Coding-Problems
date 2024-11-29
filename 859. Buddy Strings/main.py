class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        elif s == goal:
            return len(set(s)) < len(s)

        else:
            Not_Equal = []
            for i in range(len(s)):
                if s[i] == goal[i]:
                    continue
                else:
                    Not_Equal.append(i)
        
        if len(Not_Equal) == 2:
            i , j = Not_Equal
            if s[i] == goal[j] and s[j] == goal[i]:
                return True
        
        return False
