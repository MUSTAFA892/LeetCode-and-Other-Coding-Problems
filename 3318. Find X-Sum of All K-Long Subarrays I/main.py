class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        l,r = 0, k-1
        ans= []

        while r < len(nums):

            freq = Counter(nums[l:r+1])
            freq = Counter(dict(sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)))

            sub = []
            count = 0

            for key , val in freq.items():
                if count < x:
                    sub.append(key * val)
                    count += 1
                else:
                    break
            ans.append(sum(sub))
            
            l+=1 
            r+=1
            
        return ans