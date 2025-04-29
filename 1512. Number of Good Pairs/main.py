class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        
        freq = {}

        for n in nums:
            if n in freq:
                count += freq[n]
                freq[n] += 1

            else:
                freq[n] = 1

        return count 


"""        count = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1

                
        return count"""