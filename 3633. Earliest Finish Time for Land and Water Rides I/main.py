class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        early_finish = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                land_finish = max(landStartTime[i], 0) + landDuration[i]
                water_start = max(land_finish, waterStartTime[j])
                water_finish = water_start + waterDuration[j]

                early_finish = min(early_finish, water_finish)

                water_finish2 = max(waterStartTime[j], 0) + waterDuration[j]
                land_start = max(water_finish2, landStartTime[i])
                land_finish2 = land_start + landDuration[i]

                early_finish = min(early_finish, land_finish2)

        
        return early_finish