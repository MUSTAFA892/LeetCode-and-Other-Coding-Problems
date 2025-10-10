class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:

        for i in range(len(energy)-1,-1,-1):
   
            if i+k < len(energy):
                if  energy[i+k]<0:
                    energy[i] = energy[i] + energy[i+k]
                else:
                    energy[i] = energy[i] + max(0,energy[i+k])

        return max(energy)

"""        max_energy = []

        for i in range(len(energy)):
            val = 0
            for j in range(i,len(energy),k):
                val += energy[j]
                    
                    
            max_energy.append(val)

        return max(max_energy)"""
            