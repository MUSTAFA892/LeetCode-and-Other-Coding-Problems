class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        target_idx = []
        min_distance = float('inf')
        n = len(words)

        if target not in words:
            return -1

        for i in range(len(words)):
            if words[i] == target:
                right_side = (i - startIndex) % n
                left_side = (startIndex - i) % n    
                min_distance = min(min_distance, left_side, right_side)

        return min_distance