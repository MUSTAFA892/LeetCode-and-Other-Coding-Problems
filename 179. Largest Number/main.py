class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]

        str_nums.sort(key=lambda x: x*10, reverse=True)

        if str_nums[0] == "0":
            return "0"

        return ''.join(str_nums)

"""        str_nums = [str(num) for num in nums]
        max_str = ""

        for p in itertools.permutations(str_nums):
            num_str = ''.join(p)
        
            if num_str > max_str:
                max_str = num_str
        
        if max_str[0] == '0':
            return "0" 

           
        return max_str"""