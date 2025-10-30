class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        zeros = []
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)

        def stimulate(zero_index,way):
            count = 0 
            temp = nums[:]
            direction = way
            pointer = zero_index
            total = sum(temp)
            
            while 0 <= pointer < len(nums) and total >= 0:
                if temp[pointer] != 0:
                    temp[pointer] -= 1
                    direction *= -1
                    total -= 1
            
                pointer += direction
            
            
                if total == 0:
                    count += 1
                    break
                
            return count 

        for i in zeros:
            
            count += stimulate(i,1)
            count += stimulate(i,-1)

        return count            
                