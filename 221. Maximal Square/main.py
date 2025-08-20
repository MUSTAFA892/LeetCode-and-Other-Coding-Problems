class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nums = [[int(item) for item in row] for row in matrix]
        top = 0
        left = 0
        top_left = 0
        max_number = 1

#        if len(nums) == 1:
#            max_number = max(nums[0])
#            return max_number

 #       if len(nums) == 2 and max(nums[0]) == 0 and max(nums[1]) == 0:
 #           return 0
 #       
 #       if len(nums) == 4 and max(nums[0]) == 0 and max(nums[1]) == 0:
 #          return 0

        if len(nums) == 1:
            max_number = max(nums[0])
            return max_number

        has_one = any("1" in row for row in matrix)
        if not has_one:
            return 0

        
        for i in range(1,len(nums)):
            for j in range(1,len(nums[0])):
                #print('i=',i,'j=',j)
                #print(nums[i][j])
                top = nums[i-1][j]
                left = nums[i][j-1]
                top_left = nums[i-1][j-1]
                
                if nums[i][j] == 1:
                    nums[i][j] = 1 + min(top,left,top_left)
                else:
                    nums[i][j] = 0
                max_number = max(max_number,nums[i][j])
        return max_number**2