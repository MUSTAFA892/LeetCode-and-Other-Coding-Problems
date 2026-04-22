from collections import Counter, defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = defaultdict(list)
        
        for i, num in enumerate(nums):
            positions[num].append(i)

        min_distance = float('inf')

        for key in positions:
            idx = positions[key]
            
            if len(idx) < 3:
                continue

            for i in range(len(idx) - 2):
                a, b, c = idx[i], idx[i+1], idx[i+2]
                val = abs(a-b) + abs(b-c) + abs(c-a)
                min_distance = min(min_distance, val)

        if min_distance == float('inf'):
            return -1
        else:
            return min_distance