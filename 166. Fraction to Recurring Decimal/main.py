class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        str_ = []
        str_.append(str(abs(numerator) // abs(denominator)))
        remainder = abs(numerator) % abs(denominator)

        if remainder != 0:
            str_.append(".")

        count = len(str_)
        freq = {}
        
        while remainder != 0:
            if remainder in freq:
                str_.insert(freq[remainder], '(')  
                str_.append(')')  
                break
            freq[remainder] = count
            new_remainder = (remainder*10) % abs(denominator)
            str_.append(str((remainder*10) // abs(denominator)))
            remainder = new_remainder
            count += 1
        if (numerator < 0) != (denominator < 0):
            str_.insert(0,'-')
        return ''.join(str_)