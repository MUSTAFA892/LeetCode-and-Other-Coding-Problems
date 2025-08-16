class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = ""
        count = 0
        for i in str(num):
            if i == '6' and count <= 0:
                nums += '9'
                count += 1
            else:
                nums += i
        
        return int(nums)
    