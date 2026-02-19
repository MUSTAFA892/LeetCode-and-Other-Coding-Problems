class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_val = bin(n)[2:]

        if len(bin_val) == 1:
            return True

        flag = False
        for i in range(len(bin_val)-1):
            if bin_val[i] == '1' and bin_val[i +1] == '0':
                flag = True 
                
            elif bin_val[i] == '0' and bin_val[i + 1] == '1':
                flag = True
                
            else:
                return False

        return flag