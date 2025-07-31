class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        final_arr = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])   
        
        even.sort()
        odd.sort(reverse=True)

        even_idx , odd_idx = 0 , 0
    
        for i in range(len(nums)):
            if i % 2 == 0:
                final_arr.append(even[even_idx])
                even_idx += 1

            else:
                final_arr.append(odd[odd_idx])
                odd_idx += 1


        return final_arr          