class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        final_bit = [bin(i)[2:] for i in nums]

        max_len = max(len(b) for b in final_bit)
        final_bit = [b.zfill(max_len) for b in final_bit]

        bit_sum = [0] * max_len

        for b in final_bit:
            for i, bit in enumerate(b):
                bit_sum[i] += int(bit)

        ans = []
        for i in bit_sum:
            if i >= k:
                ans.append('1')
            else:
                ans.append('0')
                
        return int(''.join(ans),2)