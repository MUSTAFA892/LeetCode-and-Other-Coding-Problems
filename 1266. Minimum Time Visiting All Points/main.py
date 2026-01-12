class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0

        for i in range(1,len(points)):
            count += max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))
        return count
            
"""        count = 0
        for i in range(1, len(points)):
            val = points[i-1].copy()

            while val[0] != points[i][0] or val[1] != points[i][1]:
                count += 1

                if val[0] < points[i][0]:
                    val[0] += 1
                elif val[0] > points[i][0]:
                    val[0] -= 1

                if val[1] < points[i][1]:
                    val[1] += 1
                elif val[1] > points[i][1]:
                    val[1] -= 1

        return count"""