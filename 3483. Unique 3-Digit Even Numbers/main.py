class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0
        perm = itertools.permutations(digits,3)
        for i in set(perm):
            val = int(''.join(map(str,i)))
            if val % 2 == 0 and len(str(val)) == 3:
                count += 1
                

        return count