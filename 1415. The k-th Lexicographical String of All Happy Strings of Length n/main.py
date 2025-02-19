class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def get_happy_strings(current_str):
            if len(current_str) == n:
                result.append(current_str)
                return 
            
            for char in  'abc':
                if not current_str or current_str[-1]  != char:
                    get_happy_strings(current_str + char)
        
        result = []
        get_happy_strings('')

        if k <= len(result):
            return result[k-1]
        else:
            return ''