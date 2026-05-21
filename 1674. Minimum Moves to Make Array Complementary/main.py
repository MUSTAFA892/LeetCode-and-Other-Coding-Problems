class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            pair_sum = a + b

            diff[2] += 2

            diff[low] -= 1
            diff[high + 1] += 1

            diff[pair_sum] -= 1
            diff[pair_sum + 1] += 1

        ans = float('inf')
        curr = 0

        for target in range(2, 2 * limit + 1):
            curr += diff[target]
            ans = min(ans, curr)

        return ans

"""        min_moves = float('inf')
        n = len(nums)
        for target in range(2, 2 * limit + 1):
            
            count = 0
            
            for i in range(n // 2):
                
                first_ele = nums[i]
                second_ele = nums[n - 1 - i]
                
                pair_sum = first_ele + second_ele

                if pair_sum == target:
                    continue

                elif (
                    1 <= target - first_ele <= limit or
                    1 <= target - second_ele <= limit
                ):
                    count += 1

                else:
                    count += 2
            
            min_moves = min(min_moves, count)

        return min_moves"""
