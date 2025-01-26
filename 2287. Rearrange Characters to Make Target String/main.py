class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_count = Counter(s)
        target_count = Counter(target)
        result = float('inf')

        for char in target_count:
            result = min(result, s_count[char] // target_count[char])
        return result