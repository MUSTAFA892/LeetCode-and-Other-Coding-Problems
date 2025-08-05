class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left , right = 0 , 0
        current_size = 0
        window_size = 0

        freq_map = defaultdict(int)

        while right < len(fruits):
            freq_map[fruits[right]] += 1
            
            if len(freq_map) <= 2:
                right += 1
                current_size = right - left
                
            elif len(freq_map) > 2:
                freq_map[fruits[left]] -= 1
                if freq_map[fruits[left]] == 0:
                    del freq_map[fruits[left]]
                
                left += 1
                right += 1
                current_size = right - left

            
                
            window_size = max(window_size,current_size)
        
        return window_size