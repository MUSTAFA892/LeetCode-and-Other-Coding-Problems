    class Solution:
        def maximumSum(self, nums: List[int]) -> int:
            map_ = {}
            max_ = -1
            for num in nums:
                digit_sum = sum(int(digits) for digits in str(num))

                if digit_sum in map_:
                    map_[digit_sum].append(num)
                else:
                    map_[digit_sum] = [num]

            for val in map_.values():
                if len(val) > 1:
                    val.sort(reverse=True)
                    max_ = max(max_, val[0] + val[1])
            return max_

            """a = []
            sum_ = []
            for i in nums:
                a.append(sum(int(digit) for digit in str(i)))
                
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if a[i] == a[j]:
                        sum_.append(nums[i] + nums[j])
            
            if sum_:
                return max(sum_)
            else:
                return -1"""