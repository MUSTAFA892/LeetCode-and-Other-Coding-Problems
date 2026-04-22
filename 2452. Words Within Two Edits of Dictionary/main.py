class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        arr = []

        for i in queries:
            if i in dictionary:
                arr.append(i)
            else:
                for j in dictionary:
                    diff_count = sum(1 for c1, c2 in zip(i, j) if c1 != c2)
                    if diff_count <= 2:
                        arr.append(i)
                        break

        return arr