class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_map = {}

        for i, num in enumerate(sorted(set(arr)), start=1):
            rank_map[num] = i

        rank = [rank_map[num] for num in arr]

        return rank