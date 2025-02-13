class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        flag = False
        heapq.heapify(nums)

        if all(num>=k for num in nums):
            return 0

        while len(nums) > 0:
            flag = False

            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            new_value = min(x,y) * 2 + max(x,y)

            heapq.heappush(nums, new_value)

            count += 1

            for num in nums:
                if num >= k:
                    flag = True
                else:
                    flag = False
                    break

            if flag:
                return count
                break
        
        if not flag:
            return count

