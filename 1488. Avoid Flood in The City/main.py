class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        full_lake = {}  
        dry_lake = []

        for i in range(len(rains)):
            if rains[i] == 0:
                dry_lake.append(i)
                ans[i] = 1

            else:
                if rains[i] in full_lake:
                    flag = False
                    for j in range(len(dry_lake)):
                        if dry_lake[j] > full_lake[rains[i]]:   
                            ans[dry_lake[j]] = rains[i]
                            dry_lake.pop(j)
                            flag = True
                            break
                    
                    if not flag:
                        return []

                full_lake[rains[i]] = i
                ans[i] = -1
            
        return ans