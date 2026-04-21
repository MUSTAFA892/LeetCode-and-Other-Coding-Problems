class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l , r = 0, len(colors)-1
        max_distance = 0


        while l <= r:
            if colors[l] != colors[r]:
                distance1 = r
                distance2 = (len(colors)-1) - r
                distance = max(distance1,distance2)
                max_distance = max(max_distance,distance)
                r -= 1

            else:
                r -= 1
        return max_distance