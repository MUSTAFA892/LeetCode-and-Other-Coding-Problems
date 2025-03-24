class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}

        for idx, str_ in enumerate(strs):

            sorted_str = tuple(sorted(str_))

            if sorted_str not in grouped_anagrams:
                grouped_anagrams[sorted_str] = []
            grouped_anagrams[sorted_str].append(str_)


        ans = list(grouped_anagrams.values())

        return ans