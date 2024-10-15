import heapq
import math 

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        sum_val = 0

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        for _ in range(k):

            Top_value = -heapq.heappop(max_heap)

            sum_val += Top_value

            Top_value = math.ceil(Top_value / 3.0)

            heapq.heappush(max_heap, -Top_value)
        
        return sum_val