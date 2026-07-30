class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_ = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        arr = []

        for i in digits:
            arr.append(map_[i])
            
        result = [''.join(t) for t in list(itertools.product(*arr))]

        return result