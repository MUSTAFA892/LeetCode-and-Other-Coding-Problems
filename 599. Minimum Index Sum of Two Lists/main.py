class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float('inf')
        ans = []

        for value_list1 in range(len(list1)):
            if list1[value_list1] in list2:
                value_list2 = list2.index(list1[value_list1])
                current_sum = value_list1 + value_list2


                if current_sum < min_sum:
                    min_sum = current_sum
                    ans = [list1[value_list1]]
                
                elif current_sum == min_sum:
                    ans.append(list1[value_list1])
        
        return ans