class Solution:
    def oddString(self, words: List[str]) -> str:
        freq_map = {}
        
        def get_value(num):
            return ord(num) - ord('a')
            
        for word in words:
            arr = []
            for j in range(len(word) - 1):
                letter = get_value(word[j+1]) - get_value(word[j])
                arr.append(letter)

            key = tuple(arr)

            if key not in freq_map:
                freq_map[key] = []
            freq_map[key].append(word)

        for diff, word_list in freq_map.items():
            if len(word_list) == 1:
                return word_list[0]