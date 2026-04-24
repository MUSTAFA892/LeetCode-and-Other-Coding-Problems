class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        map_ = {}
        arr = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] not in map_:
                map_[nums[i]] = []
                
            map_[nums[i]].append(i)

        for pos in map_.values():
            total = sum(pos)
            left_sum = 0

            for i in range(len(pos)):
                right_sum = total - left_sum - pos[i]

                left = pos[i]  * i - left_sum
                right = right_sum - pos[i] * (len(pos) - i - 1)

                arr[pos[i]] = left + right

                left_sum += pos[i]

        return arr

        
"""        arr = []

        map_ = {}

        for i in range(len(nums)):
            if nums[i] not in map_:
                map_[nums[i]] = []
                
            map_[nums[i]].append(i)

        for i in range(len(nums)):
            val = map_[nums[i]]
            if len(val) <= 1:
                arr.append(0)
                
            else:
                comp  = 0
                for j in range(1,len(val)):
                    comp += abs(val[0] - val[j])    
                    
                arr.append(comp)
                temp = val[0]
                map_[nums[i]].remove(temp)
                map_[nums[i]].append(temp)
                
        return arr
                """
                
                
