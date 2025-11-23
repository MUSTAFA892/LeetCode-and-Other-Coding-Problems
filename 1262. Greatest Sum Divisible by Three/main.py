class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            rema = i % 3
            if rema not in freq:
                freq[rema] = []
            freq[rema].append(i)

        for key in freq:
            freq[key].sort()

        while sum(nums) % 3 != 0:
            rem = sum(nums) % 3              

            optionA = float('inf')
            if rem in freq and len(freq[rem]) > 0:
                optionA = freq[rem][0]       

            optionB = float('inf')
            opp = (3 - rem) % 3

            if opp in freq and len(freq[opp]) >= 2:
                optionB = freq[opp][0] + freq[opp][1]

            if optionA <= optionB:

                remove_val = freq[rem][0]
                freq[rem].pop(0)
                nums.remove(remove_val)

            else:

                remove_val1 = freq[opp][0]
                remove_val2 = freq[opp][1]
                freq[opp] = freq[opp][2:]   
                nums.remove(remove_val1)
                nums.remove(remove_val2)

        return sum(nums)
