class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        st = []
        for i in nums:
            st.append(i**2)
        return sorted(st)