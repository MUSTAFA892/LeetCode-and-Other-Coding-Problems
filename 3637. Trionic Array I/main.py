class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        change = float('inf')

        map_ = []
        for i in range(len(nums)-1):
            if True:   
                if nums[i] == nums[i+1]:
                    return False

                if nums[i] < nums[i+1]:
                    change = 1
                
                else:
                    change = 0 
                    
                map_.append(change)


        if len(map_) < 3 or map_[0] == 0 or map_[-1] == 0 or 0 not in map_: 
            return False
        
        changes = 0
        for i in range(1,len(map_)):
            if map_[i] != map_[i-1]:
                changes += 1

        if changes != 2:
            return False


        return True
