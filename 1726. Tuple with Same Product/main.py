class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ans.append(nums[i] * nums[j])
        dict_1 = Counter(ans)

        sum_ = 0

        for count in dict_1.values():
            if count > 1:
                sum_ += count * (count - 1) // 2
            
        return sum_ * 8