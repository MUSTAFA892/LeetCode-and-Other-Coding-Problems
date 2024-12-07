class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0  
        count = 1  

        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1
            else:
                chars[write_index] = chars[i - 1]
                write_index += 1
                if count > 1:
                    for digit in str(count):
                        chars[write_index] = digit
                        write_index += 1
                count = 1

        return write_index  

"""    result = []
        count = 1

        for i in range(len(chars) - 1):
            if chars[i] == chars[i+1]:
                count += 1
            else:
                result.append(chars[i])
                if count > 1:
                    result.append(str(count))
                count = 1

        result.append(chars[-1])
        if count > 1:
            result.append(str(count))
        
        for i in range(len(result)):
            chars[i] = result[i]
        return len(result)"""