class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        max_ = 0
        chunks = 0

        for i in range(n):
            max_ = max(max_, arr[i])

            if max_ == i:
                chunks += 1
        return chunks