class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return (len(nums))



"""     index = 0  #Track the index 
        for i in range(len(nums)): #Run the loop throughout the array
            if nums[i] != val: #Check if the given index element is not equal to the value
                nums[index] = nums[i] #Then change index value to i value of the array
                index+=1 # Append one in the index
        return index""" 