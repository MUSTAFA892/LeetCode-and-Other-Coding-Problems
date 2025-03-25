class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = Counter(s)
        ans = []
        sort  = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        for val , idx in sort.items():
            ans.append(val * idx)
            
        return ''.join(ans)