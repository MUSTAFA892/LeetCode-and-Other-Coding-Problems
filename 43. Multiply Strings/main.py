class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mul_val = []

        for i in range(len(num2)):
            zeros = (len(num2)-1)-i
            mul_val.append(str(int(num2[i])*int(num1))+'0'*zeros)
            
        product_val = 0
        for i in mul_val:
            product_val += int(i)

        return str(product_val)
    
"""class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mul = int(num1) * int(num2)
        return str(mul)"""