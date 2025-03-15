class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        third = float('-inf')
        stack = []

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < third:
                return True
            
            while stack and nums[i] > stack[-1]:
                third = stack.pop()
            
            stack.append(nums[i])

        return False



        """flag = False

        for i in range(0, len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                for k in range(j+1, len(nums)):
                    if nums[i]< nums[k] < nums[j]:
                        flag = True
        
        return flag"""