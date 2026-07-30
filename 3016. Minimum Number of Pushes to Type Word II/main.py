class Solution:
    def minimumPushes(self, word: str) -> int:
        map_ = Counter(word)
        word_counter = 0

        for i, ( key, val) in enumerate(map_.most_common()):
            v = (i//8) + 1
            word_counter += (v * val)

        return word_counter
            