class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:    

        e , o = 0 , 0

        for i in range(len(nums)-1, -1, -1):
            if nums[i] % 2 == 0:
                nums[i] = o
                e += 1

            else:
                nums[i] = e
                o += 1
        
        return nums 