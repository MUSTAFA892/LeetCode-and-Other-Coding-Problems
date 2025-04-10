class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans  = []
        freq = Counter(nums)

        count= 0

        for val, cou in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            ans.append(val)
            count += 1
            if count == k:    
                break


        return ans