class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        fruits_left = 0

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]:
                    baskets.remove(baskets[j])
                    break

        fruits_left = len(baskets)
        return fruits_left