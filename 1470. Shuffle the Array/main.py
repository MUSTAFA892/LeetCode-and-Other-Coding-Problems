class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a1 = nums[:n]
        a2 = nums[n:]
        ans = []
        for i in range(n):
            ans.append(a1[i])
            ans.append(a2[i])
            
        return ans
