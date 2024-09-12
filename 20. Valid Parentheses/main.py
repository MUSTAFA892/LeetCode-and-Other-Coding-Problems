class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')':'(','}':'{',']':'['}
        for brackets in s:
            if brackets in bracket_map.values():
                stack.append(brackets)
            else:
                if not stack or stack[-1] != bracket_map[brackets]:
                    return False
                stack.pop()
        return not stack