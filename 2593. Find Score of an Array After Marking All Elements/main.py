class Solution:
    def findScore(self, nums: List[int]) -> int:
        score =  0
        list_ = []
        n = len(nums)
        marked = [False] * n

        for i in range(len(nums)):
            list_.append((nums[i],i))
        list_.sort()

        for value , index in list_:
            if marked[index]:
                continue

            score += value

            marked[index] = True

            if index > 0:
                marked[index - 1] = True
            if index < n-1:
                marked[index + 1] = True

        return score
            