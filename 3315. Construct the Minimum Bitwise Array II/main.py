class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:

            if n % 2 == 0:
                ans.append(-1)
                continue

            bin_ = list(bin(n)[2:])

            idx = -1
            for i in range(len(bin_) - 1, -1, -1):
                if bin_[i] == '0':
                    idx = i
                    break

            if idx == -1:
                bin_ = bin_[1:]
            
            else:
                bin_[idx+1] = '0'

            con = int(''.join(bin_),2)
            ans.append(con) 

        return ans