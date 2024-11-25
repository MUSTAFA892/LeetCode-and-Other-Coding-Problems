class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i<n and s[i] == " ":
            i += 1
            
        if i == n:
            return 0

        sign = 1
        if s[i] == '-':
            sign = -1
            i +=1
        elif s[i] == '+':
            i+=1
            
            
        result = 0
        while i<n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        int_min , int_max = -2 ** 31 , 2 ** 31 -1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max

        return result


