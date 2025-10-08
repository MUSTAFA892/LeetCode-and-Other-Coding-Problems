class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        spell = spells.copy()

        indexed_spells = list(enumerate(spell))
        indexed_spells.sort(key=lambda x: x[1])


        spells.sort()
        potions.sort()

        spells_counter = 0
        potions_counter = len(potions) - 1

        count = 0

        while spells_counter < len(spells) :
            while potions_counter >= 0 and spells[spells_counter] * potions[potions_counter] >= success:
                potions_counter -= 1

            count = len(potions) - (potions_counter + 1)
            spell[indexed_spells[spells_counter][0]] = count
            spells_counter += 1
            count = 0
        
        return spell

"""     counter = []

        for i in spells:
            mul = []
            count = 0

            for j in potions:
                a = i * j
                if a >= success:
                    count += 1

            counter.append(count)
            count = 0
        
        return counter"""
