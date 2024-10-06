class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array
        n = len(nums)
        closest_sum = float('inf')  # Initialize closest sum to infinity

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first number
                continue
                
            lo, hi = i + 1, n - 1  # Set up two pointers

            while lo < hi:
                current_sum = nums[i] + nums[lo] + nums[hi]

                # Update closest_sum if the current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:  # Move the lower pointer up to increase the sum
                    lo += 1
                elif current_sum > target:  # Move the upper pointer down to decrease the sum
                    hi -= 1
                else:  # If we find an exact match
                    return current_sum

        return closest_sum