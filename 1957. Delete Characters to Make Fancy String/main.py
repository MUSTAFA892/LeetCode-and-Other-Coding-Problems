class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        count = 0
        previous_char = ''

        for char in s:
            if char == previous_char:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                result.append(char)

            previous_char = char
        
        return "".join(result)