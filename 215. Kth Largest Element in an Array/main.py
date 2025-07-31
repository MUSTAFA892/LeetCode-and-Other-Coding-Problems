class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(k):
            heapq.heappush(heap,nums[i])
            
        for i in range(k,len(nums)):
            min_ele_heap = heap[0]
            if min_ele_heap < nums[i]:
                heapq.heappop(heap)
                heapq.heappush(heap,nums[i])

        return heap[0]