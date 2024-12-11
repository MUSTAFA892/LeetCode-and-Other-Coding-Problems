class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def divider(max_balls):
            operations = 0
            for n in nums:
                operations += ceil(n / max_balls) - 1
                if operations > maxOperations:
                    return False
            return True

        l , r = 1 , max(nums)
        res = r
        while l < r:
            mid = (l + r) // 2
            if divider(mid):
                r = mid 
                res = r
            else:
                l = mid + 1
        return res            
                    