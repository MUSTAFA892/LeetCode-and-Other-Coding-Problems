class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = list(range(n))
        heapq.heapify(available)
        busy_rooms = []
        counts = [0] * n 

        meetings.sort()

        for i in range(len(meetings)):
            duration = abs(meetings[i][0] - meetings[i][1])
                        
            while busy_rooms and busy_rooms[0][0] <= meetings[i][0]:
                idx_pop = heapq.heappop(busy_rooms)
                heapq.heappush(available,idx_pop[1])

            if available:
                pop = heapq.heappop(available)
                heapq.heappush(busy_rooms, (meetings[i][1], pop))
                counts[pop] += 1

            else:
                closest_endTime = heapq.heappop(busy_rooms)
                new_endTime = closest_endTime[0] + duration
                heapq.heappush(busy_rooms,(new_endTime, closest_endTime[1]))
                counts[closest_endTime[1]] += 1


        return counts.index(max(counts))