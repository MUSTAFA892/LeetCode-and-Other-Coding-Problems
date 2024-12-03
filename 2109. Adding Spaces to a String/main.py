class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        slicing = 0

        for i in spaces:
            result.append(s[slicing:i])
            result.append(" ")
            slicing = i
        
        result.append(s[slicing:])
        return "".join(result)


""""        result = []
        spaces_identified = 0
        n = len(s)

        for i in range(n):
            if spaces_identified < len(spaces) and i == spaces[spaces_identified]:
                result.append(" ")
                spaces_identified += 1

            result.append(s[i])

        return "".join(result)
"""
