class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        Free_Days = 0
        Latest_End = 0

        for start , end in meetings:
            
            if start > Latest_End + 1:
                Free_Days += start - Latest_End - 1

            Latest_End = max(Latest_End,end)

        Free_Days += days - Latest_End

        return Free_Days                
        
"""        result = set()

        for start , end in meetings:

            for i in range(start,end+1):
                result.add(i)


        return days - len(result)"""
        
"""        result = set()


        for i in meetings:
            start = i[0]
            end = i[1]

            result.update(list(range(start,end+1)))


        return days - len(result)"""